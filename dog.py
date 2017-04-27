'''
How to make a valid dict key:
    __hash__
    __eq__ or __cmp__

But! I still recommend using ONLY
    int
    str
    tuple of int and/or str
    or other immutable things that are easy to compare
'''

class Dog(object):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        fmt = '{}(name={!r})'
        return fmt.format(type(self).__name__, self.name)

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def bark(self):
        print 'Woof! %s is barking' % (self.name,)


a = Dog('Fido')
b = Dog('Fido')
c = Dog('Clifford')

d = {}
d[a] = 'my dog'
