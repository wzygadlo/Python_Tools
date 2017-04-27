''' abstract.py

Inheritance is for reusing code across classes.

Mixins are GREAT!
- make programming fun and easy
  Writing a new class is just a list of capabilities

Mixins are also TERRIBLE :-(
- people accidentally instantiate the mixin
- people forget to implement required dependencies

The solution is Abstract Base Classes (ABCs).
'''

from abc import ABCMeta, abstractmethod
from collections import Sequence

class Capper(object):
    'inherit to gain uppercasing capability'

    __metaclass__ = ABCMeta
    
    def capitalize(self):
        return ''.join([c.upper() for c in self])

    @abstractmethod
    def __getitem__(self, index):
        return None

    @abstractmethod
    def __len__(self):
        return 0

class Uncapper(Sequence):
    'inherit to gain lowercasing capability'
    def uncapitalize(self):
        return ''.join([c.lower() for c in self])

class SkipSeq(Capper, Uncapper):
    '''
    A sequence that skips every other element.

        >>> skip = SkipSeq('abcdefg')
        >>> skip[0]
        'a'
        >>> skip[1]
        'c'
        >>> len(skip)
        4
    '''

    def __init__(self, sequence):
        self.seq = sequence

    def __getitem__(self, index):
        return self.seq[index * 2]

    def __len__(self):
        return (len(self.seq) + 1) // 2

class SkipTwoSeq(Capper, Uncapper):
    '''
    A sequence that keeps every third element.

        >>> skip = SkipTwoSeq('abcdefg')
        >>> skip[0]
        'a'
        >>> skip[1]
        'd'
        >>> len(skip)
        3
    '''

    def __init__(self, sequence):
        self.seq = sequence

    def __getitem__(self, index):
        return self.seq[index * 3]

    def __len__(self):
        return (len(self.seq) + 2) // 3

if __name__ == '__main__':
    import doctest
    doctest.testmod()
