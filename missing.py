'''
dict.__missing__
'''

class AngryDict(dict):
    def __missing__(self, key):
        print 'I am so angry, %r is missing!' % (key,)
        raise KeyError(key)

class ZeroDict(dict):
    def __missing__(self, key):
        return 0

class ListDict(dict):
    def __missing__(self, key):
        value = []
        self[key] = value
        return value

class DefaultFormatDict(dict):
    def __missing__(self, key):
        return '%(' + key + ')s'


class DefaultDict(dict):
    'rough sketch of collections.defaultdict'

    def __init__(self, factory, *args, **kwargs):
        self.factory = factory
        self.update(*args, **kwargs)

    def __missing__(self, key):
        value = self.factory()
        self[key] = value
        return value


class ChainDict(dict):
    '''
    dict that allows cascading lookup
    to a fallback if keys are missing
    '''
    # collections.ChainMap available in Python3

    # locals --> globals --> builtins --> NameError
    # instance --> class --> bases ... --> AttributeError
    # CWD --> $PYTHONPATH --> site-packages --> ImportError
    # $PATH --> "executable not found"
    # L1 --> L2 --> L3 --> RAM --> virtual memory --> kernel panic!

    def __init__(self, fallback, *args, **kwargs):
        self.fallback = fallback
        self.update(*args, **kwargs)

    def __missing__(self, key):
        return self.fallback[key]
    
defaults = {'bg': 'black', 'fg': 'green', 'h': 24, 'w': 40}
settings = ChainDict(defaults, {'fg': 'cyan', 'h': 40, 'w': 80})






