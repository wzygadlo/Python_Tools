'''
"Context Managers are the greatest invention
    since the subroutine" -- Raymond Hettinger


==========  ==========================  =========================
Op/Fn/Kwd   Magic Methods               Jargon
==========  ==========================  =========================
s + t       s.__add__(t)                Addable
s / t       s.__div__(t)                Divisible
>>> s       s.__repr__()
print s     s.__str__()
s[t]        s.__getitem__(t)            Indexable, Subscriptable
for t in s  s.__iter__()                Iterable
next(s)     s.next()                    Iterator
s()         s.__call__()                Callable
len(s)      s.__len__()                 Sizeable
with s:     s.__enter__() s.__exit__()  Context Manager
==========  ==========================  =========================
'''

def one():
    return 1

def two():
    return 2

registry = {int: one, str: two}

class Foo:
    def __add__(self, other):
        try:
            func = registry[type(other)]
        except KeyError:
            raise TypeError('Expected int or str')
        return func()


class ContextManager(object):
    'a generic context manager'

    def __init__(self, value):
        self.value = value

    def __enter__(self):
        print 'entering the context'
        return self.value

    def __exit__(self, etype, einstance, etraceback):
        print 'leaving the context'
        if isinstance(einstance, RuntimeError):
            print 'marking exception as handled'
            return True


class File:
    'rough sketch of a file'

    def __init__(self, filename, mode='rt'):
        'use the OS to open the file'

    def close(self):
        'use the OS to close the file'

    def __enter__(self):
        return self

    def __exit__(self, etype, einstance, etraceback):
        self.close()


class Lock:
    'rough sketch of a threading.Lock'

    def __init__(self):
        'use the OS to get a mutex'

    def acquire(self):
        '''
        use the OS to check that the mutex is unset
        and then set the mutex
        '''

    def release(self):
        'use the OS to unset the mutex'

    def __enter__(self):
        self.acquire()

    def __exit__(self, *args):
        self.release()


import os
try:
    os.remove('tmp.txt')
except OSError:
    pass # suppress the error


class Suppress(object):
    'suppress errors'

    def __init__(self, etypes):
        self.etypes = etypes

    def __enter__(self):
        return self

    def __exit__(self, etype, einstance, etraceback):
        if isinstance(einstance, self.etypes):
            return True


with Suppress(OSError):
    os.remove('tmp.txt')
        

class Closing(object):
    'turns any object into a closing context manager'
    
    def __init__(self, closeable):
        self.obj = closeable

    def __enter__(self):
        return self.obj

    def __exit__(self, *args):
        self.obj.close()


import sys

class RedirectStdout(object):
    'temporarily replace stdout with a different file-like object'

    def __init__(self, target):
        self.target = target

    def __enter__(self):
        self.old_stdout = sys.stdout
        sys.stdout = self.target
        return self

    def __exit__(self, *args):
        sys.stdout = self.old_stdout


with RedirectStdout(sys.stderr):
    print 'red'
print 'blue'


with open('topics.txt', 'w') as f:
    with RedirectStdout(f):
        help('topics')


if __name__ == '__main__':
    with ContextManager(42) as x:
        print 'inside the context'
        print x
        raise RuntimeError('oops')
        print 'last line in the context'
