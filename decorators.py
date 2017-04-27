'''
All about decorators.


Identity Function
    the output is the same as the input

Higher-order Function
    receives a function as input
    and/or returns a function as output

Pure Function
    1. always returns the same output for a given input
    2. no side-effects (only returns a value)

Wrapper Function
    uses another function ("helper")
    typically similar behavior, but improved

Factory Function
    a function that creates and returns a function

Closure
    a place to stash variables from the enclosing scope
    available on functions defined inside other functions
'''

import time, random, math
import functools

### Factory functions ##################

def pow2(x):
    return x ** 2

def make_pow(exponent):
    def power(base):
        return base ** exponent
    return power

powers = map(make_pow, range(100))

def make_logging(func):
    def logging_wrapper(*args, **kwargs):
        print 'calling', func.__name__
        print 'with', args, kwargs
        result = func(*args, **kwargs)
        print 'result was', result
        return result
    logging_wrapper.__name__ = func.__name__
    logging_wrapper.__doc__ = func.__doc__
    return logging_wrapper

def make_caching(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

maxsize = 3
def clearing_cache(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        if len(cache) >= maxsize:
            cache.clear()
        cache[args] = result
        return result
    return wrapper

def random_cache(maxsize=10):
    def decorator(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
            if args in cache:
                return cache[args]
            result = func(*args)
            if len(cache) >= maxsize:
                del cache[random.choice(list(cache))]
            cache[args] = result
            return result
        return wrapper
    return decorator


### Wrapper functions ##################

def logging_sin(x):
    print 'calling sin'
    print 'with', x
    result = math.sin(x)
    print 'result was', result
    return result

def better_sqrt(x):
    'sqrt that works on negative inputs'
    if x >= 0:
        return math.sqrt(x)
    return 1j * math.sqrt(-x)

### (Monkey) Patching ##################

import theirs

old_sqrt = math.sqrt

def patch_sqrt(x):
    'sqrt that works on negative inputs'
    if x >= 0:
        return old_sqrt(x)
    return 1j * old_sqrt(-x)

math.sqrt = patch_sqrt

theirs.sqrts([4, 81, -25, 16])

### Higher-order functions #############

def identity(x):
    return x

registry = {}

def register(func):
    registry[func.__name__] = func
    return func

def add_docstring(func):
    if func.__doc__ is None:
        func.__doc__ = 'unknown documentation'
    return func

### Normal functions ###################

@add_docstring
@register
@identity
def square(x):
    return x ** 2

# square = identity(square)
# square = register(square)
# square = add_docstring(square)

@add_docstring
@register
def power(base, exponent):
    return base ** exponent

# power = register(power)
# power = add_docstring(power)

@make_logging
@add_docstring
@register
def collatz(x):
    'half or triple plus one'
    if x % 2 == 0:
        return x // 2
    return 3 * x + 1

# collatz = register(collatz)
# collatz = add_docstring(collatz)
# collatz = make_logging(collatz)

@make_caching
def conjecture(x):
    'recursing collatz arrives at 1 eventually'
    if x < 1:
        raise ValueError('Must be positive')
    if x == 1:
        return True
    x = collatz(x)
    return conjecture(x)

@random_cache(maxsize=3)
def hardwork(x):
    print 'doing hard work!'
    time.sleep(1)
    return x + 1

# hardwork = random_cache(hardwork)
# hardwork = random_cache(maxsize=3)(hardwork)

cache = {}

def caching_hardwork(x):
    if x in cache:
        return cache[x]
    result = hardwork(x)
    cache[x] = result
    return result

