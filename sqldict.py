''' 
dict-like, backed by a SQLite database.
- persistent
- concurrency
- shareable with other languages
- introspectable
'''

from collections import MutableMapping
import sqlite3, json

class SqlDict(MutableMapping):
    'dict-like, backed by a SQLite database.'
    # Dict
    # ==========
    # key   text   <-- unique index
    # value text

    # Values will be stored in JSON-format

    def __init__(self, dbname, *args, **kwargs):
        self.dbname = dbname
        self.connection = sqlite3.connect(dbname)
        c = self.connection.cursor()
        try:
            c.execute('CREATE TABLE Dict (key text, value text)')
            c.execute('CREATE UNIQUE INDEX KeyIndex ON Dict (key)')
        except sqlite3.OperationalError:
            pass # table already exists
        self.update(*args, **kwargs)

    def __repr__(self):
        return '{}({!r}, {!r})'.format(type(self).__name__,
                                       self.dbname,
                                       self.items())

    def __getitem__(self, key):
        c = self.connection.cursor()
        c.execute('SELECT value FROM Dict WHERE key=?', (key,))
        row = c.fetchone()
        if row is None:
            raise KeyError(key)
        return json.loads(row[0])

    def __setitem__(self, key, value):
        value = json.dumps(value)
        if key in self:   # LBYL creates a race condition
            del self[key] # TODO: use a transaction
        c = self.connection.cursor()
        c.execute('INSERT INTO Dict VALUES (?, ?)', (key, value))
        self.connection.commit()

    def __delitem__(self, key):
        if key not in self:
            raise KeyError(key)
        c = self.connection.cursor()
        c.execute('DELETE FROM Dict WHERE key=?', (key,))
        self.connection.commit()

    def __len__(self):
        c = self.connection.cursor()
        c.execute('SELECT count(key) FROM Dict')
        row = c.fetchone()
        return row[0]

    def __iter__(self):
        c = self.connection.cursor()
        c.execute('SELECT key FROM Dict')
        rows = c.fetchall()
        keys = [key for (key,) in rows]
        return iter(keys)

##    Yielding from the cursor might lock the DB in some cases.
##    
##    def __iter__(self):
##        c = self.connection.cursor()
##        c.execute('SELECT key FROM Dict')
##        for row in c:
##            yield row[0]

    def copy(self):
        raise NotImplementedError(
            'Duplicate copies of a SqlDict share the same data')

    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, etype, einstance, etraceback):
        self.close()

if __name__ == '__main__':
    with SqlDict('starwars.db') as d:
        d['hero'] = 'Luke'
        d['villain'] = 'Darth'
        print d

        del d['villain']
        d['hero'] = ('Rey', 'Finn')
        print d
