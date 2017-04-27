''' filedict.py

A dictionary-like object, backed by the filesystem:
- persistent
- concurrent
- shareable with other languages
- introspectable

We will use collections.MutableMapping as our guide.
MutableMapping will enforce the dict-like interface.

An ABC is like prefabricated housing.
- you build the foundation (override the abstract methods)
- the ABC builds the house (mixin methods)
'''

from collections import MutableMapping
import os, errno, pickle

class FileDict(MutableMapping):
    'dict-like, backed by the filesystem.'
    # each FileDict stores data in a separate folder
    # key <--> filename
    # value <--> filedata

    def __init__(self, folder, *args, **kwargs):
        self.folder = folder
        try:
            os.mkdir(folder)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise # re-raise current exception
        self.update(*args, **kwargs)

    def __repr__(self):
        fmt = '{}({!r}, {!r})'
        return fmt.format(type(self).__name__,
                          self.folder,
                          self.items())

    def __delitem__(self, key):
        filepath = os.path.join(self.folder, key)
        try:
            os.remove(filepath)
        except OSError:
            raise KeyError(key)

    def __getitem__(self, key):
        filepath = os.path.join(self.folder, key)
        try:
            with open(filepath) as f:
                return pickle.load(f)
        except IOError:
            raise KeyError(key)

    def __setitem__(self, key, value):
        try:
            filepath = os.path.join(self.folder, key)
        except AttributeError:
            raise TypeError('FileDict keys must be strings')
        try:
            with open(filepath, 'w') as f:
                pickle.dump(value, f)
        except IOError:
            raise ValueError('FileDict keys must be valid filenames')

    def __len__(self):
        return len(os.listdir(self.folder))

    def __iter__(self):
        return iter(os.listdir(self.folder))

if __name__ == '__main__':
    d = FileDict('starwars')
    d['hero'] = 'Luke'
    d['villain'] = 'Darth Vader'
    print d

    del d['villain']
    d['hero'] = ('Rey', 'Finn')
    print d.keys()
    print d.values()
