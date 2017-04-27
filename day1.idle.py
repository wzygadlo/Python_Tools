Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 12:39:47) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> # Python for Engineers, Part 2
>>> # Copyright (c) 2017 Raymond Hettinger
>>> 
>>> # Instructor: Michael Selik
>>> #             mike@selik.org
>>> 
>>> str, int, float, bool
(<type 'str'>, <type 'int'>, <type 'float'>, <type 'bool'>)
>>> list, dict, set, tuple
(<type 'list'>, <type 'dict'>, <type 'set'>, <type 'tuple'>)
>>> 
>>> a = [10, 20]
>>> a[0]
10
>>> a[1]
20
>>> b = a
>>> a == b
True
>>> a
[10, 20]
>>> b
[10, 20]
>>> a[0] = 'changed'
>>> a
['changed', 20]
>>> b
['changed', 20]
>>> a is b
True
>>> 
>>> # In C, variables are like buckets -- aliases for memory locations
>>> # In Python, variables are like nametags -- references to objects
>>> 
>>> a = [10, 20]
>>> b = a
>>> 
>>> a[0] = 'changed'
>>> b
['changed', 20]
>>> 
>>> a = [10, 20]
>>> b = list(a)
>>> a is b
False
>>> a is not b
True
>>> a == b
True
>>> a[0] = 'changed'
>>> a
['changed', 20]
>>> b
[10, 20]
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> a = [10, 20]
>>> a.copy()

Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a.copy()
AttributeError: 'list' object has no attribute 'copy'
>>> [x for x in a]
[10, 20]
>>> 
>>> import copy
>>> 
>>> a[:]
[10, 20]
>>> 
>>> b = a[:]
>>> 
>>> a == b
True
>>> a is not b
True
>>> 
>>> 
>>> 
>>> a = [10, 20]
>>> a.append([30, 40])
>>> 
>>> a
[10, 20, [30, 40]]
>>> 
>>> len(a)
3
>>> 
>>> b = a[:]
>>> a == b
True
>>> a is not
SyntaxError: invalid syntax
>>> a is not b
True
>>> 
>>> a
[10, 20, [30, 40]]
>>> b
[10, 20, [30, 40]]
>>> 
>>> a[0] = 'changed'
>>> a
['changed', 20, [30, 40]]
>>> b
[10, 20, [30, 40]]
>>> 
>>> # On Win:   Alt-P, Alt-N
>>> # On Mac:   Ctrl-P, Ctrl-N
>>> 
>>> 
>>> a[2]
[30, 40]
>>> a[2][0] = 'also changed'
>>> a
['changed', 20, ['also changed', 40]]
>>> 
>>> b
[10, 20, ['also changed', 40]]
>>> 
>>> a[2]
['also changed', 40]
>>> a[2] is b[2]
True
>>> 
>>> # shallow copy does not copy nested elements
>>> # deep copy recursively copies all nested elements
>>> 
>>> b = a[:]   # shallow copy
>>> 
>>> import
SyntaxError: invalid syntax
>>> import copy
>>> copy.deepcopy(a)  # deep copy
['changed', 20, ['also changed', 40]]
>>> 
>>> 
>>> a = [10, 20, [30, 40]]
>>> b = copy.deepcopy(a)
>>> 
>>> a[2][0] = 'changed'
>>> a
[10, 20, ['changed', 40]]
>>> b
[10, 20, [30, 40]]
>>> 
>>> a[0] is b[0]
True
>>> 
>>> 
>>> None
>>> type(None)
<type 'NoneType'>
>>> 
>>> # Guido van Rossum
>>> 
>>> 
>>> None is None is None
True
>>> # Singleton
>>> True is True
True
>>> False
False
>>> 0 is 0
True
>>> 
>>> # CPython
>>> 
>>> x = 999
>>> y = 999
>>> x is y
False
>>> 
>>> x = 255
>>> y = 255
>>> x is y
True
>>> y = 256
>>> x = 256
>>> x is y
True
>>> 
>>> 
>>> 
>>> a = [2000]
>>> b = copy.deepcopy(a)
>>> 
>>> a is b
False
>>> a[0] is b[0]
True
>>> 
>>> x = 2000
>>> y = 2000
>>> x is y
False
>>> 
>>> 
>>> x = y = 100000
>>> x is y
True
>>> 
>>> 
>>> 'a' is 'a'
True
>>> int(str(10)) == 10
True
>>> int(str(10000)) is 10000
False
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> # shallow vs deep
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> 
>>> 
>>> names = ['John', 'Paul', 'George', 'Ringo']
>>> for name in names:
	print name

	
John
Paul
George
Ringo
>>> 
>>> 
>>> 
>>> for i in range(len(names)):
	print names[i]

	
John
Paul
George
Ringo
>>> 
>>> 
>>> for i, name in enumerate(names):
	print i, name

	
0 John
1 Paul
2 George
3 Ringo
>>> 
>>> # You should (almost) NEVER use the index in a for-loop
>>> 
>>> names = ['John', 'Paul', 'George', 'Ringo']
>>> 
>>> for name in sorted(names):
	print name

	
George
John
Paul
Ringo
>>> 
>>> 
>>> names = ['John', 'Paul', 'George', 'Ringo']
>>> for names in names:
	print names

	
John
Paul
George
Ringo
>>> for names in names:
	print names

	
R
i
n
g
o
>>> names = ['John', 'Paul', 'George', 'Ringo']
>>> for name in names[::-1]:
	print name

	
Ringo
George
Paul
John
>>> names = ['John', 'Paul', 'George', 'Ringo']
>>> for name in reversed(names):
	print name

	
Ringo
George
Paul
John
>>> 
>>> # enumerate, sorted, reversed
>>> 
>>> names = ['John', 'Paul', 'George', 'Ringo']
>>> roles = ['guitar', 'bass', 'guitar', 'drums']
>>> 
>>> for name, role in zip(names, roles):
	print name, role

	
John guitar
Paul bass
George guitar
Ringo drums
>>> 
>>> names.append('Pete')
>>> for name, role in zip(names, roles):
	print name, role

	
John guitar
Paul bass
George guitar
Ringo drums
>>> 
>>> import itertools
>>> itertools.izip_longest
<type 'itertools.izip_longest'>
>>> 
>>> # enumerate, sorted, reversed, zip
>>> 
>>> for size in map(len, names):
	print size

	
4
4
6
5
4
>>> # enumerate, sorted, reversed, zip, map, filter
>>> 
>>> help(map)
Help on built-in function map in module __builtin__:

map(...)
    map(function, sequence[, sequence, ...]) -> list
    
    Return a list of the results of applying the function to the items of
    the argument sequence(s).  If more than one sequence is given, the
    function is called with an argument list consisting of the corresponding
    item of each sequence, substituting None for missing values when not all
    sequences have the same length.  If the function is None, return a list of
    the items of the sequence (or a list of tuples if more than one sequence).

>>> map(pow, range(10), range(10))
[1, 1, 4, 27, 256, 3125, 46656, 823543, 16777216, 387420489]
>>> 
>>> # enumerate, sorted, reversed, zip, map, filter
>>> 
>>> zip(names, map(len, names))
[('John', 4), ('Paul', 4), ('George', 6), ('Ringo', 5), ('Pete', 4)]
>>> dict(zip(names, map(len, names)))
{'Ringo': 5, 'Pete': 4, 'Paul': 4, 'John': 4, 'George': 6}
>>> 
>>> set(map(len, names))
set([4, 5, 6])
>>> sorted(set(map(len, names)))
[4, 5, 6]
>>> 
>>> 
>>> 
>>> names
['John', 'Paul', 'George', 'Ringo', 'Pete']
>>> 
>>> map(len, name)
[1, 1, 1, 1, 1]
>>> map(len, names)
[4, 4, 6, 5, 4]
>>> 
>>> 
>>> sorted(names, key=len)
['John', 'Paul', 'Pete', 'Ringo', 'George']
>>> 
>>> max(names, key=len)
'George'
>>> min(names, key=len)
'John'
>>> 
>>> 
>>> 
>>> names
['John', 'Paul', 'George', 'Ringo', 'Pete']
>>> 
>>> 
>>> 
>>> def first(sequence):
	return sequence[0]

>>> 
>>> sorted(names, key=first)
['George', 'John', 'Paul', 'Pete', 'Ringo']
>>> 
>>> 
>>> # dict.grouping(names, key=first)
>>> 
>>> {'G': [George], 'P': ['Paul', 'Pete'], 'R': ['Ringo']}

Traceback (most recent call last):
  File "<pyshell#263>", line 1, in <module>
    {'G': [George], 'P': ['Paul', 'Pete'], 'R': ['Ringo']}
NameError: name 'George' is not defined
>>> {'G': ['George'], 'P': ['Paul', 'Pete'], 'R': ['Ringo']}
{'P': ['Paul', 'Pete'], 'R': ['Ringo'], 'G': ['George']}
>>> 
>>> 
>>> groups = {}
>>> for name in names:
	initial = first(name)
	if initial not in groups:
		groups[initial] = []
	groups[initial].append(name)

	
>>> groups
{'P': ['Paul', 'Pete'], 'R': ['Ringo'], 'J': ['John'], 'G': ['George']}
>>> 
>>> names
['John', 'Paul', 'George', 'Ringo', 'Pete']
>>> names = ['John', 'Paul', 'George', 'Ringo', 'Pete']
>>> 
>>> def first(sequence):
	return sequence[0]

>>> 
>>> 
>>> dict.from_keys(set(map(first, names)), [])

Traceback (most recent call last):
  File "<pyshell#283>", line 1, in <module>
    dict.from_keys(set(map(first, names)), [])
AttributeError: type object 'dict' has no attribute 'from_keys'
>>> 
>>> 
>>> {c: [] for c in set(map(first, names))}
{'P': [], 'J': [], 'R': [], 'G': []}
>>> groups = {c: [] for c in set(map(first, names))}
>>> 
>>> 
>>> # dict.grouping(names, key=first)      maybe coming in v3.7
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> 
>>> names = ['John', 'Paul', 'George', 'Ringo']
>>> names[:2]
['John', 'Paul']
>>> names[:-1]
['John', 'Paul', 'George']
>>> 
>>> names[:-4]
[]
>>> names[:-3]
['John']
>>> names[:-2]
['John', 'Paul']
>>> names[:-1]
['John', 'Paul', 'George']
>>> names[:-0]
[]
>>> names[:-0] # neg idx on the right-hand of a slice can NEVER get the whole list
[]
>>> -0 is 0
True
>>> names[-4:]
['John', 'Paul', 'George', 'Ringo']
>>> names[-3:]
['Paul', 'George', 'Ringo']
>>> names[-2:]
['George', 'Ringo']
>>> names[-1:]
['Ringo']
>>> names[-0:]
['John', 'Paul', 'George', 'Ringo']
>>> names[-0:] # neg idx on the left-hand of a slice can NEVER get an empty list
['John', 'Paul', 'George', 'Ringo']
>>> 
>>> 
>>> for i in range(len(names)):
	print names[:-i]

	
[]
['John', 'Paul', 'George']
['John', 'Paul']
['John']
>>> for i in range(len(names)):
	print names[:-(i+1)]

	
['John', 'Paul', 'George']
['John', 'Paul']
['John']
[]
>>> for i in range(len(names)):
	print names[-i:]

	
['John', 'Paul', 'George', 'Ringo']
['Ringo']
['George', 'Ringo']
['Paul', 'George', 'Ringo']
>>> for i in range(len(names)):
	print names[-(i+1):]

	
['Ringo']
['George', 'Ringo']
['Paul', 'George', 'Ringo']
['John', 'Paul', 'George', 'Ringo']
>>> 
>>> # Be afraid of -i in a slice. It's probably a bug
>>> 
>>> 
>>> 
>>> # Imagine 4-bit signed 2's Complement Integers
>>> 
>>> # Binary 		Decimal
>>> # 0 000		0
>>> # 0 001 		1
>>> # 0 010 		2
>>> # 0 011 		3
>>> # ...
>>> # 0 111 		7
>>> # 1 000 		-8
>>> # 1 001 		-7
>>> # 1 010		-6
>>> # ...
>>> # 1 111 		-1
>>> 
>>> 
>>> # IEEE 754: floating point specification
>>> 
>>> # sign * 1.mantissa ** (1024 - exponent)
>>> 
>>> # 64-bit floats
>>> # 1 bit for the sign
>>> # 10 bits for the exponent
>>> # 52 bits for the mantissa/significand
>>> 
>>> 0.5 + 0.25
0.75
>>> 1.1 + 5.5
6.6
>>> 1.1 + 2.2
3.3000000000000003
>>> 
>>> [0.1]
[0.1]
>>> [0.1] * 10
[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
>>> sum([0.1] * 10)
0.9999999999999999
>>> 
>>> 
>>> (0.5).as_integer_ratio()
(1, 2)
>>> (0.1).as_integer_ratio()
(3602879701896397, 36028797018963968)
>>> 
>>> a = 1.1 + 2.2
>>> b = 3.3
>>> 
>>> a == b
False
>>> 
>>> epsilon = 1e-9
>>> epsilon
1e-09
>>> 
>>> def is_close(x, y, epsilon=1e-9):
	return abs(x - y) < epsilon

>>> is_close(a, b)
True
>>> 
>>> import math
>>> math.isclose

Traceback (most recent call last):
  File "<pyshell#377>", line 1, in <module>
    math.isclose
AttributeError: 'module' object has no attribute 'isclose'
>>> 
>>> math.isclose # available in Python 3

Traceback (most recent call last):
  File "<pyshell#379>", line 1, in <module>
    math.isclose # available in Python 3
AttributeError: 'module' object has no attribute 'isclose'
>>> 
>>> # break until 11:05am
>>> 
>>> 
>>> # www.github.com/selik-teaching/2017-04-24
>>> 
>>> 
>>> map(None, [1, 2])
[1, 2]
>>> map(None, [1, 2, 3], [1, 2])
[(1, 1), (2, 2), (3, None)]
>>> None?
SyntaxError: invalid syntax
>>> help(None)
Help on NoneType object:

class NoneType(object)
 |  Methods defined here:
 |  
 |  __hash__(...)
 |      x.__hash__() <==> hash(x)
 |  
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)

>>> 
>>> help(map)
Help on built-in function map in module __builtin__:

map(...)
    map(function, sequence[, sequence, ...]) -> list
    
    Return a list of the results of applying the function to the items of
    the argument sequence(s).  If more than one sequence is given, the
    function is called with an argument list consisting of the corresponding
    item of each sequence, substituting None for missing values when not all
    sequences have the same length.  If the function is None, return a list of
    the items of the sequence (or a list of tuples if more than one sequence).

>>> 
>>> 
>>> None(4)

Traceback (most recent call last):
  File "<pyshell#395>", line 1, in <module>
    None(4)
TypeError: 'NoneType' object is not callable
>>> 
>>> 
>>> 
>>> 
>>> 5 / 3
1
>>> 5.0 / 3.0
1.6666666666666667
>>> 
>>> 5 // 3
1
>>> 
>>> from __future__ import division
>>> 
>>> 
>>> 5 / 3
1.6666666666666667
>>> 
>>> 5 // 3
1
>>> 
>>> 
>>> 5 // 2
2
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> -5 // 2
-3
>>> from __future__ print_function
SyntaxError: invalid syntax
>>> from __future__ import print_function
>>> 
>>> 
>>> print(5)
5
>>> from __future__ import braces
SyntaxError: not a chance (<pyshell#421>, line 1)
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> import antigravity
>>> 
>>> 
>>> from __future__ import barry_as_FLUFL
SyntaxError: future feature barry_as_FLUFL is not defined (<pyshell#428>, line 1)
>>> 
>>> 
>>> # spam
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> print(5, 6)
(5, 6)
>>> from __future__ import print_function
>>> print(5, 6)
5 6
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> 
>>> # Python 2:    str, unicode
>>> # Python 3:    bytes, str
>>> 
>>> 
>>> 
>>> 
>>> 'jalapeno'
'jalapeno'
>>> print 'jalapeno'
jalapeno
>>> print u'jalape\u00f1o'
jalapeño
>>> 
>>> # utf-8   Unicode Tranformation Function 8
>>> 
>>> # utf-8   Unicode Transformation Function 8
>>> 
>>> 
>>> 
>>> message = 'a secret message'
>>> storage = message.encode('rot-13')
>>> storage
'n frperg zrffntr'
>>> storage.decode('rot-13')
u'a secret message'
>>> 
>>> # text --[encode]--> storage/transmit
>>> # storage/transmit --[decode]--> text
>>> 
>>> # data --[decode: mpeg4, wmv]--> video
>>> # data --[decode: mp3, wav]--> audio
>>> # data --[decode: png, jpg, tiff]--> image
>>> 
>>> # data --[decode: utf-8]--> text
>>> 
>>> data = '\x50\x40\x67\xff\xa0'
>>> data.decode('utf-8')

Traceback (most recent call last):
  File "<pyshell#470>", line 1, in <module>
    data.decode('utf-8')
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/encodings/utf_8.py", line 16, in decode
    return codecs.utf_8_decode(input, errors, True)
UnicodeDecodeError: 'utf8' codec can't decode byte 0xff in position 3: invalid start byte
>>> data.decode('utf-8', 'ignore')
u'P@g'
>>> data.decode('utf-8', 'replace')
u'P@g\ufffd\ufffd'
>>> print data.decode('utf-8', 'replace')
P@g��
>>> 
>>> 
>>> print u'jalape\u00f1o'
jalapeño
>>> data = u'jalape\u00f1o'.encode('utf-8')
>>> data
'jalape\xc3\xb1o'
>>> data.decode('utf-8')
u'jalape\xf1o'
>>> print data.decode('utf-8')
jalapeño
>>> data.decode('utf-16')

Traceback (most recent call last):
  File "<pyshell#481>", line 1, in <module>
    data.decode('utf-16')
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/encodings/utf_16.py", line 16, in decode
    return codecs.utf_16_decode(input, errors, True)
UnicodeDecodeError: 'utf16' codec can't decode byte 0x6f in position 8: truncated data
>>> data.decode('latin-1')
u'jalape\xc3\xb1o'
>>> print data.decode('latin-1')
jalapeÃ±o
>>> 
>>> 
>>> 
>>> # text --[encode: utf-8]-->
>>> # text --[encode: utf-8]--> storage/transmit
>>> # data --[decode: utf-8]--> text
>>> 
>>> 
>>> print u'\u00f1'
ñ
>>> print u'\U0000f1'
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 0-7: truncated \UXXXXXXXX escape
>>> print u'\U000000f1'
ñ
>>> print u'\N{snowman}\N{comet}\N{umbrella}'
☃☄☂
>>> print u'\N{poop}'
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 0-7: unknown Unicode character name
>>> 
>>> print u'\N{BLACK SQUARE}'
■
>>> 
>>> 
>>> # Python2:   str, unicode
>>> # Python3:   bytes, str
>>> 
>>> data.decode('utf-8', 'ignore')
u'jalape\xf1o'
>>> 
>>> 
>>> 
>>> 
>>> # Python 3.6
>>> 
>>> 
>>> 
>>> int, list, str, float
(<type 'int'>, <type 'list'>, <type 'str'>, <type 'float'>)
>>> bool
<type 'bool'>
>>> 
>>> 
>>> int, str, float
(<type 'int'>, <type 'str'>, <type 'float'>)
>>> 
>>> bool
<type 'bool'>
>>> 
>>> # 0, [], None
>>> 
>>> True = 1
>>> False = 0
>>> 
>>> bool
<type 'bool'>
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> True + 5
6
>>> isinstance(True, int)
True
>>> 
>>> False * 5
0
>>> 
>>> names = ['John', 'Paul', 'George', 'Ringo']
>>> 
>>> [len(name) for name in names]
[4, 4, 6, 5]
>>> [len(name) % 2 for name in names]
[0, 0, 0, 1]
>>> [len(name) % 2 == 0 for name in names]
[True, True, True, False]
>>> sum([len(name) % 2 == 0 for name in names])
3
>>> 
>>> 
>>> 
>>> True and True
True
>>> True and False
False
>>> 
>>> False and True
False
>>> 
>>> False and 5
False
>>> 
>>> True or 0
True
>>> 
>>> 5 or 0
5
>>> 
>>> # and/or are shortcut (aka short-circuit) keywords
>>> 
>>> 5 and 0
0
>>> 0 and 5
0
>>> 5 and 10
10
>>> 
>>> def foo():
	print 'foo'
	return True

>>> def foo():
	print 'foo'
	return 1

>>> def bar():
	print 'bar'
	return 0

>>> foo() and bar()
foo
bar
0
>>> bar() and foo()
bar
0
>>> foo() or bar()
foo
1
>>> bar() or foo()
bar
foo
1
>>> 
>>> # ternary expression:         (<condition> ? <true> : <false>)
>>> 
>>> 
>>> sunshine = True
>>> 
>>> if sunshine:
	print 'picnic'
else:
	print 'inside'

	
picnic
>>> 
>>> 
>>> 'picnic' if sunshine else 'cafeteria'
'picnic'
>>> # <true> if <condition> else <false>
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> tuple
<type 'tuple'>
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> names = ['John', 'Paul', 'George', 'Ringo']
>>> 
>>> 
>>> names = ['John', 'Paul', 'George', 'Ringo']
>>> 
>>> 
>>> any_len_gt_5 = False
>>> for name in names:
	if len(name) > 5:
		any_len_gt_5 = True

		
>>> any_len_gt_5
True
>>> 
>>> any_len_gt_5 = True
>>> for name in names:
	if len(name) > 5:
		any_len_gt_5 = False

		
>>> any_len_gt_5
False
>>> 
>>> [name for name in names]
['John', 'Paul', 'George', 'Ringo']
>>> [len(name) for name in names]
[4, 4, 6, 5]
>>> [len(name) > 5 for name in names]
[False, False, True, False]
>>> sum([len(name) > 5 for name in names])
1
>>> any([len(name) > 5 for name in names])
True
>>> sum([len(name) > 5 for name in names]) > 3
False
>>> any([len(name) > 5 for name in names])
True
>>> 
>>> 
>>> 
>>> all_len_gt_3 = True
>>> for name in name:
	if len(name) <= 3:
		all_len_gt_3 = False

		
>>> all_len_gt_3
False
>>> for name in names:
	if len(name) <= 3:
		all_len_gt_3 = False

		
>>> all_len_gt_3 = True
>>> for name in names:
	if len(name) <= 3:
		all_len_gt_3 = False

		
>>> all_len_gt_#

Traceback (most recent call last):
  File "<pyshell#642>", line 1, in <module>
    all_len_gt_#
NameError: name 'all_len_gt_' is not defined
>>> all_len_gt_3
True
>>> 
>>> all([len(name) > 3 for name in names])
True
>>> 
>>> 
>>> # (almost) NEVER use a flag variable in a for-loop
>>> # They're too error-prone for accidentally flipping True/False
>>> 
>>> any, all
(<built-in function any>, <built-in function all>)
>>> 
>>> any([1, 1, 0, 5])
True
>>> all([1, 2, 3, 4])
True
>>> 
>>> 
>>> 
>>> completed = True
>>> for name in names:
	if name[0] == 'P':
		completed = False
		break

	
>>> completed
False
>>> 
>>> 
>>> 
>>> import random
>>> random.random()
0.41710478287460095
>>> random.randrange(5)
0
>>> random.randrange(5)
3
>>> random.randrange(5)
0
>>> range(5)
[0, 1, 2, 3, 4]
>>> range(5, 10)
[5, 6, 7, 8, 9]
>>> range(5, 50, 10)
[5, 15, 25, 35, 45]
>>> 
>>> random.randint(0, 5)
0
>>> random.randint(0, 5)
0
>>> random.randint(0, 5)
0
>>> random.randint(0, 5)
1
>>> random.randint(0, 5)
4
>>> random.randrange(5)
0
>>> random.choice('abc')
'a'
>>> random.choice('abc')
'a'
>>> random.choice('abc')
'c'
>>> random.choice('aaaaaaaaaabc')
'a'
>>> random.choice('aaaaaaaaaabc')
'a'
>>> random.choice('aaaaaaaaaabc')
'a'
>>> 
>>> 
>>> random.randrange(5)
4
>>> [random.randrange(5)] * 10
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
>>> [random.randrange(5) for i in range(10)]
[2, 4, 3, 3, 3, 4, 1, 2, 4, 0]
>>> 
>>> for n in [random.randrange(5) for i in range(10)]:
	if n == 0:
		break
	print n

	
4
>>> for n in [random.randrange(5) for i in range(10)]:
	if n == 0:
		break
	print n

	
>>> for n in [random.randrange(5) for i in range(10)]:
	if n == 0:
		break
	print n

	
>>> for n in [random.randrange(5) for i in range(10)]:
	if n == 0:
		break
	print n

	
4
4
2
>>> for n in [random.randrange(5) for i in range(10)]:
	if n == 0:
		break
	print n

	
4
>>> for n in [random.randrange(10) for i in range(10)]:
	if n == 0:
		break
	print n

	
4
1
2
4
2
5
6
9
2
2
>>> for n in [random.randrange(10) for i in range(10)]:
	if n == 0:
		break
	print n

	
2
7
7
7
5
>>> for n in [random.randrange(10) for i in range(10)]:
	if n == 0:
		break
	print n

	
3
>>> for n in [random.randrange(10) for i in range(10)]:
	if n == 0:
		break
	print n

	
2
7
4
9
6
>>> for n in [random.randrange(10) for i in range(10)]:
	if n == 0:
		break
	print n

	
4
5
3
7
>>> for n in [random.randrange(10) for i in range(10)]:
	if n == 0:
		break
	print n

	
1
5
3
>>> for n in [random.randrange(10) for i in range(10)]:
	if n == 0:
		break
	print n

	
8
>>> for n in [random.randrange(10) for i in range(10)]:
	if n == 0:
		break
	print n

	
9
1
2
1
8
6
5
2
6
7
>>> 
>>> completed = True
>>> for n in [random.randrange(10) for i in range(10)]:
	if n == 0:
		completed = False
		break
	print n

	
4
8
6
8
6
6
9
4
5
1
>>> completed
True
>>> 
>>> 
>>> '''

LOOP:
	IF break_condition() THEN GOTO BREAK
	do()
	IF loop_condition() THEN GOTO LOOP
	                    ELSE GOTO COMPLETED

BREAK:
	broken()
	GOTO AFTER

COMPLETED:
	completed()

AFTER:
	after()
'''
'\n\nLOOP:\n\tIF break_condition() THEN GOTO BREAK\n\tdo()\n\tIF loop_condition() THEN GOTO LOOP\n\t                    ELSE GOTO COMPLETED\n\nBREAK:\n\tbroken()\n\tGOTO AFTER\n\nCOMPLETED:\n\tcompleted()\n\nAFTER:\n\tafter()\n'
>>> for n in [random.randrange(10) for i in range(10)]:
	if n == 0:
		break
	print n
else:
	print 'completed the loop without breaking'

	
>>> for n in [random.randrange(10) for i in range(10)]:
	if n == 0:
		break
	print n
else:
	print 'completed the loop without breaking'

	
5
5
4
9
5
5
1
8
6
9
completed the loop without breaking
>>> 
>>> 
>>> 
>>> any, all
(<built-in function any>, <built-in function all>)
>>> # (almost) NEVER use a flag variable in a for-loop:    any, all, else
>>> 
>>> # loop-never-ran   still requires a flag variable or sentinel
>>> for x in []:
	print x

	
>>> 
>>> 
>>> 
>>> try:
	x = 1 + 1
	print x
except TypeError:
	print 'error!'

	
2
>>> try:
	x = 1 + '1'
	print x
except TypeError:
	print 'error!'

	
error!
>>> try:
	x = 1 + 1
except TypeError:
	print 'error!'
else:
	print x

	
2
>>> try:
	x = 1 + 1
except TypeError:
	print 'error!'
else: # no exception
	print x

	
2
>>> try:
	x = 1 + 1
	print x
except TypeError:
	print 'error!'

	
2
>>> 
>>> 
>>> # with
>>> 
>>> 
>>> 
>>> f = open('data/dialogue.txt')
>>> text = f.read()
>>> f.close()
>>> 
>>> f = open('data/dialogue.txt')
>>> try:
	text = f.read()
finally:
	f.close()

	
>>> 
>>> 
>>> import threading
>>> lock = threading.Lock()
>>> 
>>> lock.acquire()
True
>>> try:
	print '"critical section" using a shared resource'
finally:
	lock.release()

	
"critical section" using a shared resource
>>> 
>>> 
>>> 
>>> with open('data/dialogue.txt') as f:
	text = f.read()

	
>>> with lock:
	print 'critical section'

	
critical section
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> # lunch until 1:20pm
>>> 
>>> 
>>> # Python 2, a for-loop is nearly identical to a list comprehension
>>> 
>>> x = 'global'
>>> 
>>> print sum([x for x in range(10)])
45
>>> x
9
>>> 
>>> x = 'global'
>>> print sum(x for x in range(10))
45
>>> x
'global'
>>> 
>>> 
>>> # Python3
>>> sum([x for x in range(10)])
45
>>> x
9
>>> 
>>> 
>>> 
>>> 
>>> 
>>> numbers = []
>>> 
>>> 
>>> squares = []
>>> for x in range(1000):
	squares.append(x ** 2)

	
>>> squares = [x ** 2 for x in range(1000)]
>>> 
>>> 
>>> squares = [x ** 2 for x in range(1000)]
>>> 
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> 
>>> 
>>> def foo():
	squares = []
	for x in range(1000):
		squares.append(x)

		
>>> def bar():
	squares = [x ** 2 for x in range(1000)]

	
>>> import dis
>>> dis.dis(foo)
  2           0 BUILD_LIST               0

              3 STORE_FAST               0 (squares)

  3           6 SETUP_LOOP              33 (to 42)
              9 LOAD_GLOBAL              0 (range)
             12 LOAD_CONST               1 (1000)
             15 CALL_FUNCTION            1
             18 GET_ITER            
        >>   19 FOR_ITER                19 (to 41)
             22 STORE_FAST               1 (x)

  4          25 LOAD_FAST                0 (squares)
             28 LOAD_ATTR                1 (append)
             31 LOAD_FAST                1 (x)
             34 CALL_FUNCTION            1
             37 POP_TOP             
             38 JUMP_ABSOLUTE           19
        >>   41 POP_BLOCK           
        >>   42 LOAD_CONST               0 (None)
             45 RETURN_VALUE        
>>> 
>>> dis.dis(bar)
  2           0 BUILD_LIST               0
              3 LOAD_GLOBAL              0 (range)
              6 LOAD_CONST               1 (1000)
              9 CALL_FUNCTION            1
             12 GET_ITER            
        >>   13 FOR_ITER                16 (to 32)
             16 STORE_FAST               0 (x)
             19 LOAD_FAST                0 (x)
             22 LOAD_CONST               2 (2)
             25 BINARY_POWER        
             26 LIST_APPEND              2
             29 JUMP_ABSOLUTE           13
        >>   32 STORE_FAST               1 (squares)
             35 LOAD_CONST               0 (None)
             38 RETURN_VALUE        
>>> 
>>> import timeit
>>> import profile
>>> 
>>> import trace
>>> 
>>> 
>>> 
>>> 
>>> int, str, bool, float
(<type 'int'>, <type 'str'>, <type 'bool'>, <type 'float'>)
>>> list
<type 'list'>
>>> 
>>> tuple
<type 'tuple'>
>>> 
>>> 
>>> (1, 2, 3)
(1, 2, 3)
>>> (1, 2)
(1, 2)
>>> (1)
1
>>> (1,)
(1,)
>>> 
>>> []
[]
>>> {}
{}
>>> ()
()
>>> set()
set([])
>>> 
>>> {1, 1, 2}
set([1, 2])
>>> 
>>> 
>>> t = 1, 2
>>> t
(1, 2)
>>> 
>>> a, b = t
>>> 
>>> a
1
>>> b
2
>>> a, b = 'ab'
>>> a
'a'
>>> b
'b'
>>> a, b = [10, 20]
>>> a
10
>>> b
20
>>> a, b = {1, 2}
>>> a
1
>>> b
2
>>> a, b = {'a': 1, 'b': 2}
>>> a
'a'
>>> b
'b'
>>> a, b, c = {'a': 1, 'b': 2, 'c': 3}
>>> a
'a'
>>> b
'c'
>>> c
'b'
>>> 
>>> # list is ordered
>>> # tuple is frozen, ordered
>>> # dict is labeled
>>> # set is a bag of values
>>> 
>>> 
>>> import collections
>>> collections.OrderedDict
<class 'collections.OrderedDict'>
>>> 
>>> 
>>> 
>>> a = 5
>>> b = 10
>>> 
>>> tmp = a
>>> a = b
>>> b = tmp
>>> 
>>> del tmp
>>> 
>>> a
10
>>> b
5
>>> 
>>> 
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> p = v = a = 1
>>> 
>>> def update_p(p, v, a):
	return p + v

>>> def update_v(p, v, a):
	return v + a

>>> def update_a(p, v, a):
	return p

>>> p = update_p(p, v, a)
>>> v = update_v(p, v, a)
>>> a = update_a(p, v, a)
>>> 
>>> p, v, a
(2, 2, 2)
>>> 
>>> p = update_p(p, v, a)
>>> v = update_v(p, v, a)
>>> a = update_a(p, v, a)
>>> 
>>> p, v, a
(4, 4, 4)
>>> 
>>> 
>>> p = v = a = 1
>>> 
>>> tmp_p = update_p(p, v, a)
>>> tmp_v = update_v(p, v, a)
>>> tmp_a = update_a(p, v, a)
>>> 
>>> p = tmp_p
>>> v = tmp_v
>>> a = tmp_a
>>> 
>>> p, v, a
(2, 2, 1)
>>> 
>>> 
>>> 
>>> a, b = 5, 10
>>> 
>>> a, b = b, a
>>> 
>>> # Illusion of Simultaneous Assignment
>>> 
>>> p, v, a = update_p(p, v, a), update_v(p, v, a), update_a(p, v, a)
>>> p, v, a = update_p(p, v, a), update_v(p, v, a), update_a(p, v, a)
>>> p, v, a
(16, 14, 4)
>>> 
>>> 
>>> p = v = a = 1
>>> p, v, a = update_p(p, v, a), update_v(p, v, a), update_a(p, v, a)
>>> p, v, a = update_p(p, v, a), update_v(p, v, a), update_a(p, v, a)
>>> p, v, a = update_p(p, v, a), update_v(p, v, a), update_a(p, v, a)
>>> p, v, a
(7, 5, 4)
>>> 
>>> 
>>> 
>>> 
>>> tmp = a
>>> b = a
>>> a = tmp
>>> 
>>> 
>>> a, b = 5, 10
>>> 
>>> tmp = a
>>> b = a
>>> a = tmp
>>> 
>>> a, b
(5, 5)
>>> 
>>> 
>>> a, b = 5, 10
>>> a, b = b, a
>>> 
>>> 
>>> # no sentence fragments, no run-on sentences
>>> 
>>> a, b, a = 10, 20, 30
>>> a
30
>>> 
>>> # Don't break the illusion: don't repeat variables on the left
>>> 
>>> a, b = 10, 20
>>> a = 30
>>> 
>>> 
>>> import random
>>> 
>>> a, b, c = random.random(), random.random(), random.random()
>>> a == b == c
False
>>> 
>>> # Don't break the illusion: use only "pure" functions on the right
>>> 
>>> '''
Pure Function:
	1. always returns the same output for a given input
	2. has no side-effects (only returns a value)
'''
'\nPure Function:\n\t1. always returns the same output for a given input\n\t2. has no side-effects (only returns a value)\n'
>>> 
>>> import math
>>> math.sqrt(4)
2.0
>>> math.sqrt(4)
2.0
>>> math.sqrt(4)
2.0
>>> 
>>> import time
>>> time.time()
1493038992.926272
>>> time.time()
1493038995.315116
>>> 
>>> time.sleep(2)
>>> print time.sleep(2)
None
>>> 
>>> 
>>> a, b, c = time.time(), time.time(), time.time()
>>> a == b == c
False
>>> 
>>> while not a == b == c:
	a, b, c = time.time(), time.time(), time.time()

	
>>> a
1493039114.560641
>>> b
1493039114.560641
>>> c
1493039114.560641
>>> 
>>> # {   brace
>>> # [   bracket
>>> # (   parethenesis
>>> 
>>> while a != b != c:
	a, b, c = time.time(), time.time(), time.time()

	
>>> a
1493039114.560641
>>> b
1493039114.560641
>>> c
1493039114.560641
>>> a, b, c = range(3)
>>> while a != b != c:
	a, b, c = time.time(), time.time(), time.time()

	
>>> a
1493039204.309594
>>> b
1493039204.309594
>>> c
1493039204.309594
>>> a = 1
>>> b = 2
>>> b = 2
>>> a != b != c
True
>>> c = 2
>>> a != b != c
False
>>> 
>>> 
>>> a != b and b != c
False
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> for i in range(5):
	print i

	
0
1
2
3
4
>>> 
>>> 
>>> 
>>> # simultaneous assignment
>>> 
>>> 
>>> a, b = 1, 2, 3

Traceback (most recent call last):
  File "<pyshell#1103>", line 1, in <module>
    a, b = 1, 2, 3
ValueError: too many values to unpack
>>> a, b = 1,

Traceback (most recent call last):
  File "<pyshell#1104>", line 1, in <module>
    a, b = 1,
ValueError: need more than 1 value to unpack
>>> 
>>> 
>>> 
>>> a, b, rest = range(10)

Traceback (most recent call last):
  File "<pyshell#1108>", line 1, in <module>
    a, b, rest = range(10)
ValueError: too many values to unpack
>>> a, b, *rest = range(10)
SyntaxError: invalid syntax
>>> 
>>> 
>>> def foo(a, b, *rest):
	print a
	print b
	print rest

	
>>> foo(1, 2, 3, 4, 5)
1
2
(3, 4, 5)
>>> 
>>> 
>>> 
>>> foo(*range(10))
0
1
(2, 3, 4, 5, 6, 7, 8, 9)
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> person = ('Mike', 'Boston', 34)
>>> person
('Mike', 'Boston', 34)
>>> 
>>> people = [person, ('Raymond', 'San Jose', 0x34)]
>>> people
[('Mike', 'Boston', 34), ('Raymond', 'San Jose', 52)]
>>> 
>>> 
>>> from collections import namedtuple
>>> 
>>> namedtuple('Person', 'name', 'town', 'age')
class Person(tuple):
    'Person(name,)'

    __slots__ = ()

    _fields = ('name',)

    def __new__(_cls, name,):
        'Create new instance of Person(name,)'
        return _tuple.__new__(_cls, (name,))

    @classmethod
    def _make(cls, iterable, new=tuple.__new__, len=len):
        'Make a new Person object from a sequence or iterable'
        result = new(cls, iterable)
        if len(result) != 1:
            raise TypeError('Expected 1 arguments, got %d' % len(result))
        return result

    def __repr__(self):
        'Return a nicely formatted representation string'
        return 'Person(name=%r)' % self

    def _asdict(self):
        'Return a new OrderedDict which maps field names to their values'
        return OrderedDict(zip(self._fields, self))

    def _replace(_self, **kwds):
        'Return a new Person object replacing specified fields with new values'
        result = _self._make(map(kwds.pop, ('name',), _self))
        if kwds:
            raise ValueError('Got unexpected field names: %r' % kwds.keys())
        return result

    def __getnewargs__(self):
        'Return self as a plain tuple.  Used by copy and pickle.'
        return tuple(self)

    __dict__ = _property(_asdict)

    def __getstate__(self):
        'Exclude the OrderedDict from pickling'
        pass

    name = _property(_itemgetter(0), doc='Alias for field number 0')


<class '__main__.Person'>
>>> Person = namedtuple('Person', 'name', 'town', 'age')
class Person(tuple):
    'Person(name,)'

    __slots__ = ()

    _fields = ('name',)

    def __new__(_cls, name,):
        'Create new instance of Person(name,)'
        return _tuple.__new__(_cls, (name,))

    @classmethod
    def _make(cls, iterable, new=tuple.__new__, len=len):
        'Make a new Person object from a sequence or iterable'
        result = new(cls, iterable)
        if len(result) != 1:
            raise TypeError('Expected 1 arguments, got %d' % len(result))
        return result

    def __repr__(self):
        'Return a nicely formatted representation string'
        return 'Person(name=%r)' % self

    def _asdict(self):
        'Return a new OrderedDict which maps field names to their values'
        return OrderedDict(zip(self._fields, self))

    def _replace(_self, **kwds):
        'Return a new Person object replacing specified fields with new values'
        result = _self._make(map(kwds.pop, ('name',), _self))
        if kwds:
            raise ValueError('Got unexpected field names: %r' % kwds.keys())
        return result

    def __getnewargs__(self):
        'Return self as a plain tuple.  Used by copy and pickle.'
        return tuple(self)

    __dict__ = _property(_asdict)

    def __getstate__(self):
        'Exclude the OrderedDict from pickling'
        pass

    name = _property(_itemgetter(0), doc='Alias for field number 0')


>>> Person = namedtuple('Person', 'name', 'town', 'age')
class Person(tuple):
    'Person(name,)'

    __slots__ = ()

    _fields = ('name',)

    def __new__(_cls, name,):
        'Create new instance of Person(name,)'
        return _tuple.__new__(_cls, (name,))

    @classmethod
    def _make(cls, iterable, new=tuple.__new__, len=len):
        'Make a new Person object from a sequence or iterable'
        result = new(cls, iterable)
        if len(result) != 1:
            raise TypeError('Expected 1 arguments, got %d' % len(result))
        return result

    def __repr__(self):
        'Return a nicely formatted representation string'
        return 'Person(name=%r)' % self

    def _asdict(self):
        'Return a new OrderedDict which maps field names to their values'
        return OrderedDict(zip(self._fields, self))

    def _replace(_self, **kwds):
        'Return a new Person object replacing specified fields with new values'
        result = _self._make(map(kwds.pop, ('name',), _self))
        if kwds:
            raise ValueError('Got unexpected field names: %r' % kwds.keys())
        return result

    def __getnewargs__(self):
        'Return self as a plain tuple.  Used by copy and pickle.'
        return tuple(self)

    __dict__ = _property(_asdict)

    def __getstate__(self):
        'Exclude the OrderedDict from pickling'
        pass

    name = _property(_itemgetter(0), doc='Alias for field number 0')


>>> Person = namedtuple('Person', ['name', 'town', 'age'])
>>> Person = namedtuple('Person', ['name', 'town', 'age'])
>>> 
>>> 
>>> # class statement
>>> # 1. create class obj
>>> # 2. attach metadata   __name__, __doc__
>>> # 3. assign to var
>>> 
>>> # namedtuple
>>> # 1. create class obj
>>> # 2. attach metadata
>>> 
>>> Person = namedtuple('Person', ['name', 'town', 'age'])
>>> Person
<class '__main__.Person'>
>>> 
>>> Person('Mike', 'Boston', 34)
Person(name='Mike', town='Boston', age=34)
>>> 
>>> a = Person('Mike', 'Boston', 34)
>>> a[0]
'Mike'
>>> a.name
'Mike'
>>> 
>>> 
>>> 
>>> namedtuple('Point', ['x', 'y
		     
SyntaxError: EOL while scanning string literal
>>> namedtuple('Point', 'x y')
<class '__main__.Point'>
>>> Point = namedtuple('Point', 'x y')
>>> origin = Point(0, 0)
>>> a = Point(3, 4)
>>> 
>>> 
>>> class Point(Point):
	def distance(self, other):
		x = self.x - other.x
		y = self.y - other.y
		return math.sqrt(x ** 2 + y ** 2)

	
>>> origin = Point(0, 0)
>>> a = Point(3, 4)
>>> a.distance(origin)

Traceback (most recent call last):
  File "<pyshell#1178>", line 1, in <module>
    a.distance(origin)
  File "<pyshell#1175>", line 5, in distance
    return math.sqrt(x ** 2 + y ** 2)
NameError: global name 'math' is not defined
>>> import math
>>> a.distance(origin)
5.0
>>> 
>>> class Point(namedtuple('Point', 'x y')):
	def distance(self, other):
		x = self.x - other.x
		y = self.y - other.y
		return math.sqrt(x ** 2 + y ** 2)

	
>>> a = Point(3, 4)
>>> origin = Point(0, 0)
>>> a.distance(origin)
5.0
>>> 
>>> # class statement
>>> # class statement: 1 create obj, 2 metadata, 3 assign
>>> # namedtuple:      1 create obj, 2 metadata
>>> 
>>> 
>>> # def statement: 1 create obj, 2 metadata, 3 assign
>>> # lambda         1 create obj
>>> 
>>> lambda x: x ** 2
<function <lambda> at 0x10385f2a8>
>>> 
>>> sq = lambda x: x ** 2
>>> sq(5)
25
>>> 
>>> sorted('asFE Q@DSFFEWFasdfasdfsdfasf')
[' ', '@', 'D', 'E', 'E', 'F', 'F', 'F', 'F', 'Q', 'S', 'W', 'a', 'a', 'a', 'a', 'd', 'd', 'd', 'f', 'f', 'f', 'f', 's', 's', 's', 's', 's']
>>> sorted(set('asFE Q@DSFFEWFasdfasdfsdfasf'))
[' ', '@', 'D', 'E', 'F', 'Q', 'S', 'W', 'a', 'd', 'f', 's']
>>> sorted(set('asFE Q@DSFFEWFasdfasdfsdfasf'), key=str.lower)
[' ', '@', 'a', 'D', 'd', 'E', 'F', 'f', 'Q', 'S', 's', 'W']
>>> 
>>> 
>>> names = ['John', 'Paul', 'George', 'Ringo']
>>> 
>>> names = ['John', 'Paul', 'George', 'Ringo']
>>> sorted(names, key=len)
['John', 'Paul', 'Ringo', 'George']
>>> sorted(names, key=str.lower)
['George', 'John', 'Paul', 'Ringo']
>>> sorted(names, key=lambda s: s[-1])
['George', 'Paul', 'John', 'Ringo']
>>> 
>>> 
>>> 
>>> 
>>> 
>>> dict
<type 'dict'>
>>> 
>>> 
>>> 
>>> import pandas as pd
>>> 
>>> pd.DataFrame({'a': [1, 2, 3], 'b': 'abc'})
   a    b
0  1  abc
1  2  abc
2  3  abc
>>> pd.DataFrame({'a': [1, 2, 3], 'b': list('abc')})
   a  b
0  1  a
1  2  b
2  3  c
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> import numpy as np
>>> 
>>> 
>>> bool('hello')
True
>>> bool('false')
True
>>> bool('False')
True
>>> bool([True, False])
True
>>> bool([False])
True
>>> bool(np.array([]))
False
>>> bool(np.array([1, 2]))

Traceback (most recent call last):
  File "<pyshell#1237>", line 1, in <module>
    bool(np.array([1, 2]))
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
>>> bool(np.array([1]))
True
>>> bool(np.array([False]))
False
>>> 
>>> bool([False])
True
>>> 
>>> 
>>> 
>>> sorted('fasdflkdjdasf')
['a', 'a', 'd', 'd', 'd', 'f', 'f', 'f', 'j', 'k', 'l', 's', 's']
>>> sorted('fasdflkdjdasf', reverse=True)
['s', 's', 'l', 'k', 'j', 'f', 'f', 'f', 'd', 'd', 'd', 'a', 'a']
>>> sorted('fasdflkdjdasf', reverse='a')

Traceback (most recent call last):
  File "<pyshell#1247>", line 1, in <module>
    sorted('fasdflkdjdasf', reverse='a')
TypeError: an integer is required
>>> sorted('fasdflkdjdasf', reverse=1)
['s', 's', 'l', 'k', 'j', 'f', 'f', 'f', 'd', 'd', 'd', 'a', 'a']
>>> sorted('fasdflkdjdasf', reverse=True)
['s', 's', 'l', 'k', 'j', 'f', 'f', 'f', 'd', 'd', 'd', 'a', 'a']
>>> sorted('fasdflkdjdasf', reverse=5)
['s', 's', 'l', 'k', 'j', 'f', 'f', 'f', 'd', 'd', 'd', 'a', 'a']
>>> 
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> 
>>> # {'a': 1, 'b': 2, 'c': 3}
>>> # {}
>>> 
>>> 
>>> array = []
>>> size = 8
>>> 
>>> array = [None] * size
>>> array
[None, None, None, None, None, None, None, None]
>>> 
>>> item = ('a', 1)
>>> key, value = item
>>> key
'a'
>>> value
1
>>> 
>>> array[0] = item
>>> array
[('a', 1), None, None, None, None, None, None, None]
>>> 
>>> item = ('b', 2)
>>> array[1] = item
>>> array
[('a', 1), ('b', 2), None, None, None, None, None, None]
>>> 
>>> item = ('a', 10)
>>> 
>>> # O(N)
>>> 
>>> 
>>> # Dict insert/lookup:   O(1)
>>> 
>>> array = [None] * size
>>> item = ('a', 1)
>>> array
[None, None, None, None, None, None, None, None]
>>> 
>>> ord('a')
97
>>> 
>>> hash('a')
12416037344
>>> hash('a') % size
0
>>> 
>>> item = ('a', 1)
>>> key, value = item
>>> hash(key) % size
0
>>> 
>>> array[abs(hash(key)) % size] = item
>>> array
[('a', 1), None, None, None, None, None, None, None]
>>> 
>>> item = ('b', 2)
>>> key, value = item
>>> array[abs(hash(key)) % size] = item
>>> 
>>> item = ('c', 3}
SyntaxError: invalid syntax
>>> item = ('c', 3)
>>> key, value = item
>>> array[abs(hash(key)) % size] = item
>>> 
>>> array
[('a', 1), None, ('c', 3), ('b', 2), None, None, None, None]
>>> 
>>> {'a': 1, 'b': 2, 'c': 3}
{'a': 1, 'c': 3, 'b': 2}
>>> 
>>> abs(hash('a')) % size
0
>>> abs(hash('i')) % size
0
>>> 
>>> array = [[] for i in range(size)]
>>> 
>>> def insert(key, value):
	bucket = abs(hash(key)) % size
	item = key, value
	bucket.append(item)

	
>>> insert('a', 1)

Traceback (most recent call last):
  File "<pyshell#1325>", line 1, in <module>
    insert('a', 1)
  File "<pyshell#1324>", line 4, in insert
    bucket.append(item)
AttributeError: 'int' object has no attribute 'append'
>>> def insert(key, value):
	bucket = array[abs(hash(key)) % size]
	item = key, value
	bucket.append(item)

	
>>> size = 8
>>> array = [[] for i in range(size)]
>>> insert('a', 1)
>>> array
[[('a', 1)], [], [], [], [], [], [], []]
>>> insert('i', 9)
>>> array
[[('a', 1), ('i', 9)], [], [], [], [], [], [], []]
>>> 
>>> 
>>> size *= 4
>>> tmp = array
>>> array = [[] for i in range(size)]
>>> for bucket in tmp:
	for item in bucket:
		key = item[0]
		array[abs(hash(key)) % size] = item

		
>>> array
[('a', 1), [], [], [], [], [], [], [], ('i', 9), [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
>>> tmp
[[('a', 1), ('i', 9)], [], [], [], [], [], [], []]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> d
{'a': 1, 'c': 3, 'b': 2}
>>> d.keys()
['a', 'c', 'b']
>>> 
>>> 
>>> d
{'a': 1, 'c': 3, 'b': 2}
>>> {}
{}
>>> dict()
{}
>>> dict(a=1, b=2, c=3)
{'a': 1, 'c': 3, 'b': 2}
>>> 
>>> dict([('a', 1), ('b', 2)])
{'a': 1, 'b': 2}
>>> 
>>> dict(d)
{'a': 1, 'c': 3, 'b': 2}
>>> 
>>> d.update(d)
>>> d
{'a': 1, 'c': 3, 'b': 2}
>>> 
>>> 
>>> dict.fromkeys('abc', 0)
{'a': 0, 'c': 0, 'b': 0}
>>> dict.fromkeys('abc')
{'a': None, 'c': None, 'b': None}
>>> dict.fromkeys('abc', [])
{'a': [], 'c': [], 'b': []}
>>> d = dict.fromkeys('abc', [])
>>> d['a'].append(1)
>>> d
{'a': [1], 'c': [1], 'b': [1]}
>>> 
>>> dict.fromkeys(range(10), ())
{0: (), 1: (), 2: (), 3: (), 4: (), 5: (), 6: (), 7: (), 8: (), 9: ()}
>>> 
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> d.keys()
['a', 'c', 'b']
>>> 
>>> d.update(dict.fromkeys(range(15)))
>>> d
{0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: None, 11: None, 12: None, 13: None, 14: None, 'a': 1, 'c': 3, 'b': 2}
>>> d.keys()
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 'a', 'c', 'b']
>>> d.update(dict.fromkeys(range(60)))
>>> d.keys()
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 'b', 'a', 'c']
>>> 
>>> 
>>> hash('abc')
1453079729188098211
>>> hash(1)
1
>>> hash(2)
2
>>> 
>>> 
>>> 
>>> # <true> if <condition> else <false>
>>> 
>>> # try <expression> except <handler>
>>> # try <expression> except <type>: <handler>
>>> 
>>> try:
	x + 1
except:
	print 'handled'

	
handled
>>> x

Traceback (most recent call last):
  File "<pyshell#1404>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> try:
	x 1
except:
	print 'handled'
	
SyntaxError: invalid syntax
>>> try:
	x + 1
except TypeError:
	print 'handled'

	

Traceback (most recent call last):
  File "<pyshell#1407>", line 2, in <module>
    x + 1
NameError: name 'x' is not defined
>>> 
>>> 
>>> 
>>> import os
>>> os.remove('tmp.txt')

Traceback (most recent call last):
  File "<pyshell#1412>", line 1, in <module>
    os.remove('tmp.txt')
OSError: [Errno 2] No such file or directory: 'tmp.txt'
>>> 
>>> 
>>> if os.path.exists('tmp.txt'):
	os.remove('tmp.txt')

	
>>> try:
	os.remove('tmp.txt')
except OSError:
	pass # file already gone

>>> 
>>> 
>>> 
>>> d = dict(a=1, b=2, c=3)
>>> d
{'a': 1, 'c': 3, 'b': 2}
>>> d['a']
1
>>> 
>>> d['z']

Traceback (most recent call last):
  File "<pyshell#1430>", line 1, in <module>
    d['z']
KeyError: 'z'
>>> d.get('z', 0)
0
>>> d.get('z')
>>> help(d.get)
Help on built-in function get:

get(...)
    D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.

>>> 
>>> 
>>> d.setdefault('z', 0)
0
>>> d
{'a': 1, 'c': 3, 'b': 2, 'z': 0}
>>> 
>>> help(d.setdefault)
Help on built-in function setdefault:

setdefault(...)
    D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D

>>> 
>>> # dict.get_and_insert_if_missing
>>> 
>>> 
>>> 
>>> d.setdefault('c', 0)
3
>>> d
{'a': 1, 'c': 3, 'b': 2, 'z': 0}
>>> 
>>> # 2 hard problems in computing:
>>> # 1. cache invalidation
>>> # 2. naming things
>>> # 3. off-by-one errors
>>> 
>>> # 2 hard problems in networks
>>> # 2. guaranteed ordering of messages
>>> # 1. exactly once processing
>>> # 2. guaranteed ordering of messages
>>> 
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> 
>>> # http://github.com/selik-teaching/2017-04-24
>>> # .../blob/master/data/dialogue.txt
>>> 
>>> 
>>> # C:\Python27\data\dialogue.txt
>>> # ~/pyclass/data/dialogue.txt
>>> 
>>> open('data/dialogue.txt')
<open file 'data/dialogue.txt', mode 'r' at 0x102538660>
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/words.py", line 11, in <module>
    counts[word] += 1
KeyError: "Who's"
>>> line
"Who's there?\n"
>>> word
"Who's"
>>> counts
{}
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/words.py", line 11, in <module>
    counts[word] = counts[word] + 1
KeyError: "Who's"
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/words.py", line 15, in <module>
    counts[word] = counts[word] + 1
KeyError: "Who's"
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
>>> counts['the']
953
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
>>> counts['the']
953
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
[1, 1, 1]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
[953, 627, 612]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
[('zone,', 1), ('youth:', 1), ('youth,', 4)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
[('the', 953), ('and', 627), ('of', 612)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
[('the', 953), ('and', 627), ('of', 612)]
>>> 
>>> 
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
[('the', 953), ('and', 627), ('of', 612)]
>>> 
>>> 
>>> len(counts)
7529
>>> 
>>> 
>>> s = set()
>>> s.add(1)
>>> s
set([1])
>>> s.add(1)
>>> s
set([1])
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
[('the', 953), ('and', 627), ('of', 612)]

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/words.py", line 29, in <module>
    words[initial].add(word)
KeyError: 'W'
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
[('the', 953), ('and', 627), ('of', 612)]
>>> 
>>> 
>>> words['v']

Traceback (most recent call last):
  File "<pyshell#1489>", line 1, in <module>
    words['v']
KeyError: 'v'
>>> words
{}
>>> 
>>> 
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
[('the', 953), ('and', 627), ('of', 612)]
>>> 
>>> 
>>> 
>>> line
'Go, bid the soldiers shoot.'
>>> word
'shoot.'
>>> initial
's'
>>> words.get(initial, set())
set([])
>>> words.get(initial, set()).add(word)
>>> words
{}
>>> 
>>> set().add(word)
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
[('the', 953), ('and', 627), ('of', 612)]
>>> 
>>> 
>>> 
>>> words['v']
set(['visage', 'vile', 'violets', 'voyage;', 'vain', 'violent', 'very--pajock.', 'vacancy', 'villanous,', 'virtue,', 'vow', 'vantage.', 'valiant', 'violet', 'valenced', 'voyage,', 'vapours.', 'vows,', 'varnish', 'villain,', 'violets,', 'vengeance!', 'vanquisher;', 'virgin', 'vouchers,', 'vulgar', 'visit', 'verse', 'venom,', 'villain?', 'vigour', 'view;', 'vantage', 'vows:', 'vows;', 'venom', 'verity', 'validity;', 'vouchers', 'voice:', 'voice;', 'very', 'villain;', 'visitation', 'violence,', 'vicious', 'virtues', 'voice,', 'vouch', 'vengeance', 'virtue', 'villain!', 'vice', 'variable', 'violence;', 'ventages', 'vast', "venom'd", 'volume', 'vailed', 'visage,', 'villanies,--', 'villain', 'vouchsafe', 'virtue;', 'very,', 'violence', 'valour,', 'vial,', 'vulgar.', 'villany!', 'visitation?', 'vision', 'volley.', 'voice', "vanish'd", 'vows', 'view'])
>>> len(words)
53
>>> words['v']
set(['visage', 'vile', 'violets', 'voyage;', 'vain', 'violent', 'very--pajock.', 'vacancy', 'villanous,', 'virtue,', 'vow', 'vantage.', 'valiant', 'violet', 'valenced', 'voyage,', 'vapours.', 'vows,', 'varnish', 'villain,', 'violets,', 'vengeance!', 'vanquisher;', 'virgin', 'vouchers,', 'vulgar', 'visit', 'verse', 'venom,', 'villain?', 'vigour', 'view;', 'vantage', 'vows:', 'vows;', 'venom', 'verity', 'validity;', 'vouchers', 'voice:', 'voice;', 'very', 'villain;', 'visitation', 'violence,', 'vicious', 'virtues', 'voice,', 'vouch', 'vengeance', 'virtue', 'villain!', 'vice', 'variable', 'violence;', 'ventages', 'vast', "venom'd", 'volume', 'vailed', 'visage,', 'villanies,--', 'villain', 'vouchsafe', 'virtue;', 'very,', 'violence', 'valour,', 'vial,', 'vulgar.', 'villany!', 'visitation?', 'vision', 'volley.', 'voice', "vanish'd", 'vows', 'view'])
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
[('the', 953), ('and', 627), ('of', 612)]
>>> words['v']
set(['visage', 'vile', 'violets', 'voyage;', 'vain', 'violent', 'very--pajock.', 'vacancy', 'villanous,', 'virtue,', 'vow', 'vantage.', 'valiant', 'violet', 'valenced', 'voyage,', 'vapours.', 'vows,', 'varnish', 'villain,', 'violets,', 'vengeance!', 'vanquisher;', 'virgin', 'vouchers,', 'vulgar', 'visit', 'verse', 'venom,', 'villain?', 'vigour', 'view;', 'vantage', 'vows:', 'vows;', 'venom', 'verity', 'validity;', 'vouchers', 'voice:', 'voice;', 'very', 'villain;', 'visitation', 'violence,', 'vicious', 'virtues', 'voice,', 'vouch', 'vengeance', 'virtue', 'villain!', 'vice', 'variable', 'violence;', 'ventages', 'vast', "venom'd", 'volume', 'vailed', 'visage,', 'villanies,--', 'villain', 'vouchsafe', 'virtue;', 'very,', 'violence', 'valour,', 'vial,', 'vulgar.', 'villany!', 'visitation?', 'vision', 'volley.', 'voice', "vanish'd", 'vows', 'view'])
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
[('the', 953), ('and', 627), ('of', 612)]
>>> words['v']
set(['visage', 'vile', 'violets', 'voyage;', 'vain', 'violent', 'very--pajock.', 'vacancy', 'villanous,', 'virtue,', 'vow', 'vantage.', 'valiant', 'violet', 'valenced', 'voyage,', 'vapours.', 'vows,', 'varnish', 'villain,', 'violets,', 'vengeance!', 'vanquisher;', 'virgin', 'vouchers,', 'vulgar', 'visit', 'verse', 'venom,', 'villain?', 'vigour', 'view;', 'vantage', 'vows:', 'vows;', 'venom', 'verity', 'validity;', 'vouchers', 'voice:', 'voice;', 'very', 'villain;', 'visitation', 'violence,', 'vicious', 'virtues', 'voice,', 'vouch', 'vengeance', 'virtue', 'villain!', 'vice', 'variable', 'violence;', 'ventages', 'vast', "venom'd", 'volume', 'vailed', 'visage,', 'villanies,--', 'villain', 'vouchsafe', 'virtue;', 'very,', 'violence', 'valour,', 'vial,', 'vulgar.', 'villany!', 'visitation?', 'vision', 'volley.', 'voice', "vanish'd", 'vows', 'view'])
>>> 
>>> 
>>> 'hello' in words
False
>>> words['hello']
set([])
>>> 'hello' in words
True
>>> 
>>> 
>>> line
'Go, bid the soldiers shoot.'
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
[('the', 953), ('and', 627), ('of', 612)]

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/words.py", line 37, in <module>
    chain[last].append(word)
NameError: name 'last' is not defined
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
[('the', 953), ('and', 627), ('of', 612)]

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/words.py", line 37, in <module>
    chain[last].append(word)
NameError: name 'last' is not defined
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
[('the', 953), ('and', 627), ('of', 612)]
>>> 
>>> chain[None]
["Who's"]
>>> chain['dead']
['hour,', 'Did', 'vast', 'corse,', 'dog,', 'body?', 'body', 'and', 'and', "men's", 'body.', 'and', 'To']
>>> len(chain['dead'])
13
>>> chain['dead']
['hour,', 'Did', 'vast', 'corse,', 'dog,', 'body?', 'body', 'and', 'and', "men's", 'body.', 'and', 'To']
>>> 
>>> chain['dead'].count('and')
3
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
[('the', 953), ('and', 627), ('of', 612)]
Guildenstern?
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
[('the', 953), ('and', 627), ('of', 612)]
trifle,
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
fifty,
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
uncle,
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
somewhat
scanter
of
good
Cornelius,
and
bellowed
that
done,
that
great
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
There; my heart of nature's livery, That I cannot. I have
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
vows: these are fire; Doubt truth is as this machine is
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
eye!
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
disappointed, unanel'd, No more, ha?
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
still; For the cannoneer without, The associates tend, and so, God save heaven?
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
ghost!
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
presence and ears.
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
repent?
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
against some means this, my father, with you:--why do we coted them Of all tears:--why she, before his head Of all the morning air; Brief let you have done you e'en so?
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
Millions of the levies, The natural magic and forehead of nature, crescent, does your grace and his fines, his infusion of fame, Go thy father's death, his pledge.
>>> 
>>> 
>>> def tree():
	return defaultdict(tree)

>>> t = tree()
>>> t['a']
defaultdict(<function tree at 0x1005052a8>, {})
>>> t['b']
defaultdict(<function tree at 0x1005052a8>, {})
>>> t['b']['c']
defaultdict(<function tree at 0x1005052a8>, {})
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
Thence to gain a murder sanctuarize; Revenge his conceit?
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
remainder thus.
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
yet methinks I do you love is counter, you lay him So crimeful and fear-surprised eyes, distraction in's rouse; There is some term To assume my dear brother's wife; man go to show him: Be soft society and wife; I have no less becomes it!
>>> # Colorless green ideas sleep furiously
>>> 
>>> 
>>> chain['dead']
['hour,', 'Did', 'vast', 'corse,', 'dog,', 'body?', 'body', 'and', 'and', "men's", 'body.', 'and', 'To']
>>> chain['and']
['unfold', 'Marcellus,', 'speak', 'myself,', 'wonder.', 'warlike', 'will', 'look', 'true', 'jump', 'scope', 'tell', 'most', 'heraldry,', 'full,', 'there', 'diet,', 'this,', 'the', 'romage', 'is', 'palmy', 'the', 'gibber', 'dews', 'the', 'earth', 'countrymen.--', 'grace', 'speak!', 'shrill-sounding', 'erring', 'of', 'so', 'do', 'by', 'I', 'that', 'our', 'a', 'with', 'dole,--', 'out', 'for', 'bed-rid,', 'full', 'we', 'you,', 'let', 'all', 'favour', 'wishes', 'pardon.', 'at', 'my', 'less', 'the', 'commendable', 'the', "unschool'd:", 'is', 'who', 'think', 'comfort', 'our', 'a', 'unforced', 'resolve', 'unprofitable,', 'gross', 'earth!', 'yet,', 'your', 'Bernardo,', 'middle', 'with', 'stately', 'fear-surprised', 'speak', 'good,', 'did', 'twelve,', 'the', 'a', 'suppliance', 'bulk,', 'soul', 'health', 'yielding', 'place', 'danger', 'liquid', 'thorny', 'reckless', 'their', 'station', 'generous', 'friend,', 'remember', 'you', 'bounteous:', 'your', 'pious', 'an', 'takes', 'the', 'trumpet', 'west', "tax'd", 'with', 'indeed', 'marrow', 'forts', 'ministers', 'marble', 'we', 'tormenting', 'purged', 'combined', 'blood.', 'most', 'unnatural.', 'gifts,', 'to', 'alleys', 'wholesome', 'loathsome', 'damned', 'sting', 'observation', 'volume', 'smile,', 'be', 'part:', 'desire', 'desire,', 'for', 'whirling', 'soldiers,', 'night,', 'earth,', 'mercy', 'friending', 'these', 'who,', 'where', 'finding', 'drift', 'his', "so:'", 'there', 'usual', 'most', 'liberty.', 'outbreak', 'country.', "'gentleman.'", 'of', 'with', 'advice,', 'down-gyved', 'held', 'down,', 'profound', 'denied', 'judgment', 'Guildenstern!', 'havior,', 'to', 'good', 'profit', 'gentle', 'gentle', 'our', 'helpful', 'to', 'bring', 'source', 'our', 'desires.', 'impotence', 'in', 'allowance', 'think', 'madam,', 'time', 'time.', 'outward', 'now', 'the', 'obedience,', 'surmise.', 'my', 'place,', 'honourable.', 'dumb,', 'then', 'shoulder]', 'I', 'carters.', 'truly', 'plum-tree', 'that', 'potently', 'sanity', 'suddenly', 'my', 'dungeons,', 'count', 'I', 'light', 'our', 'outstretched', 'sure,', 'there', 'queen', 'by', 'direct', 'your', 'queen', 'indeed', 'pestilent', 'moving', 'admirable!', 'hither', 'target;', 'the', 'profit,', 'are', 'so', 'dare', 'the', 'the', 'his', 'those', 'ceremony:', 'aunt-mother', 'you', 'the', 'no', 'then,', 'mistress!', 'others,', 'by', 'thereabout', 'black', 'impasted', 'damned', 'fire,', 'good', 'wind', 'with', 'matter,', 'the', 'fellies', 'down,', 'for', 'all', 'has', 'brief', 'who', 'dignity:', 'insert', 'look', 'peasant', 'his', 'all', 'the', 'appal', 'amaze', 'ears.', 'muddy-mettled', 'most', 'blows', 'lack', 'hell,', 'the', 'perhaps', 'my', 'dangerous', 'see', 'it', 'myself,', 'arrows', 'by', 'the', 'scorns', 'the', 'sweat', 'moment', 'fair,', 'heaven?', 'quickly', 'you', 'you', 'nick-name', 'make', 'rose', 'the', 'wretched,', 'most', 'harsh;', 'feature', 'the', 'countries', 'commencement', 'beget', 'noise:', 'now,', 'is,', 'the', 'body', 'pressure.', 'heard', 'that', 'bellowed', 'not', 'shows', 'that', 'clothe', 'rewards', 'blest', 'judgment', 'I', 'was', 'my', 'not', 'for', "Tellus'", 'Hymen', 'moon', 'from', 'love', 'shortly', 'haply', 'fates', 'repose', 'night!', 'hope!', 'it', 'hence', 'fain', 'we', 'your', 'worse.', 'begin.', 'time', 'dire', 'writ', 'a', 'now', 'start', 'my', 'admiration.', 'stealers.', 'thumb,', 'it', 'there', 'presently.', "'tis", 'by.', 'by.', 'by', 'hell', 'soul', 'religious', 'feed', 'peculiar', 'armour', 'rest', "adjoin'd;", 'warrant', 'wisely', 'my', 'retain', 'we', 'forehead', 'for', 'salary,', 'course', 'am', "season'd", 'know', 'black', 'stood', 'him.', 'sit', 'bloody', 'marry', 'bulwark', 'blush', 'sweet', 'compound', 'thunders', 'on', 'command;', 'a', 'what', 'grained', 'making', 'a', 'the', 'patches,--', 'hover', 'passion,', 'her', 'stands', 'flame', 'cause', 'film', 'woo', 'good', 'this', 'minister.', 'will', 'worse', 'secrecy,', 'my', "'t", 'most', 'wind,', 'out', 'this', 'skill,', 'excuse.', 'bring', 'dismay.', 'not', 'go', 'all', 'to', 'even,', 'we', 'your', 'cat', 'the', 'every', 'mother', 'wife;', 'wife', 'so,', 'done', 'red', 'thy', 'with', 'twenty', 'peace,', 'shows', 'market', 'feed?', 'after,', 'god-like', 'will', 'strength', 'means', 'charge', 'tender', 'unsure', 'danger', 'my', 'trick', 'continent', 'hems,', 'beats', 'nods,', 'gestures', 'staff,', 'gone,', 'gone;', "donn'd", 'by', 'fie', 'so', 'he', 'unwholesome', 'whispers,', 'we', 'her', 'as', 'ear.', 'props', 'tongues,', 'grace,', 'foe,', 'loser?', 'a', 'virtue', 'where', 'didst', 'there', 'remembrance', 'columbines:', "here's", 'affliction,', 'to', 'judge', 'me:', 'all', 'in', 'repair', 'Guildenstern', 'with', 'so', 'for', 'soul,', 'dull', 'we', 'mighty,', 'more', 'no', 'tell', 'that', 'that,', 'careless', 'his', 'graveness.', 'served', 'demi-natured', 'tricks,', 'exercise', 'beg', 'fire', 'delays', 'free', 'in', 'means', 'dry--', 'long', 'herself', 'indued', 'therefore', 'finds', 'an', 'drown', 'drown', 'the', 'grave-makers:', 'unyoke.', 'could', 'now', 'knocked', 'a', 'a', 'his', 'will', 'the', 'double', 'breadth', 'must', 'of', 'calves', 'therefore', 'yet', 'say', 'sent', 'boy,', 'your', 'twenty', 'now,', 'tell', 'likelihood', 'why', "turn'd", 'mark.', 'pebbles', 'the', 'burial.', 'such', 'unpolluted', 'dead,', 'makes', 'rash,', 'so', 'dog', 'that', 'in', "England's", 'goblins', "labour'd", 'knowing', 'what', 'Rosencrantz', 'fell', 'whored', 'my', "is't", 'fertile:', 'his', 'hot', 'great', 'yet', 'his', 'rareness,', 'who', 'dagger.', 'poniards,', 'so:', 'of', 'three', 'him,', 'it', 'the', 'the', 'outward', 'through', 'winnowed', 'do', 'queen', 'all', 'say', 'take', 'exception', 'will', 'precedent', 'scant', 'by.', "envenom'd:", 'my', 'tremble', 'my', 'less,', 'Guildenstern', 'you', 'unnatural', 'forced', 'errors,', 'the']
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
('am.', 'Rosencrantz') and

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/words.py", line 50, in <module>
    word = random.choice(chain[word])
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/random.py", line 275, in choice
    return seq[int(self.random() * len(seq))]  # raises IndexError if seq is empty
IndexError: list index out of range
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
fashion and

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/words.py", line 51, in <module>
    word = random.choice(chain[word])
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/random.py", line 275, in choice
    return seq[int(self.random() * len(seq))]  # raises IndexError if seq is empty
IndexError: list index out of range
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
mad as he.
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
estate may not that way tend; Nor what he leaves, what is't to leave betimes?
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
one must in your motion you are welcome to Elsinore.
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
hands Unite commutual in most great affliction of spirit, hath sent me to a radiant angel link'd, Will sate itself in a shape of heaven, And that your grace hath laid on twelve for nine; and it doth well appear unto our state-- But to recover the wind is northerly.
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
are friends, scholars and soldiers, Give me my father!
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
Examples gross as earth exhort me: Witness this army of such things that it is very sultry,--as 'twere,--I cannot tell how.
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
the native hue of resolution Is sicklied o'er with the dream of his business, that he means No more to undertake it, I will forestall their repair hither, and say it is common for the very flame of thy star; This must be 'se offendendo;' it cannot be else.
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
charge you: come your tardy son to chide, That, lapsed in time and passion, lets go by The important acting of your brain: This bodiless creation ecstasy Is very cunning of the air, invulnerable, And our vain blows malicious mockery.
>>> 
>>> 
>>> len(chain)
23711
>>> 
>>> random.choice(list(chain))
('follow', 'him.')
>>> random.choice(list(chain))
('Nay,', 'but,')
>>> random.choice(list(chain))
('the', 'grapple')
>>> random.choice(list(chain))
('Well,', 'good')
>>> 
>>> 
>>> chain.items()[:2]
[(('death,', 'anon'), ['the']), (("beast,'--", 'it'), ['is'])]
>>> 
>>> 
>>> random.choice(list(chain))
('as', 'it')
>>> random.choice(list(chain))
('performance,', "'Twere")
>>> random.choice(list(chain))
('the', 'soul')
>>> chain['dead', 'and']
['gone,', 'gone;', "turn'd"]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/words.py", line 55, in <module>
    train()
  File "/Users/mike/teaching/2017-04-24/words.py", line 42, in train
    chain[last].append(word)
UnboundLocalError: local variable 'last' referenced before assignment
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/words.py", line 56, in <module>
    walk()
  File "/Users/mike/teaching/2017-04-24/words.py", line 47, in walk
    for word in last:
UnboundLocalError: local variable 'last' referenced before assignment
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
To business with the dream of passion, Could force his soul may be so in Denmark: So, uncle, there you are.
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/words.py", line 56, in <module>
    walk()
  File "/Users/mike/teaching/2017-04-24/words.py", line 47, in walk
    for word in last:
UnboundLocalError: local variable 'last' referenced before assignment
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
world! the paragon of animals!
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/words.py", line 56, in <module>
    walk()
  File "/Users/mike/teaching/2017-04-24/words.py", line 46, in walk
    last = random.choice(list(chain))
NameError: global name 'chain' is not defined
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
cheer in prison be my offer, not thy mind, nor let thy wiseness fear: hold off thy hand.
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
Wherein, they say, you spirits oft walk in death, Have burst their cerements; why the sepulchre, Wherein we saw thee quietly inurn'd, Hath oped his ponderous and marble jaws, To cast beyond ourselves in passion we propose, The passion ending, doth the purpose of playing, whose end, both at the stake.
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
should take it: for it cannot be else.
>>> 
>>> import words
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
his weapon; but in my thoughts.
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
not saw the air to stick: So, as a woodcock to mine uncle's bed; Assume a virtue, if you have of us, Put your bonnet to his shameful lust The will of my business.
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/words.py", line 56, in <module>
    chain = train('data/dialogue.txt', 3)
  File "/Users/mike/teaching/2017-04-24/words.py", line 42, in train
    last = last[1:] + word
TypeError: can only concatenate tuple (not "str") to tuple
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
may play the fool

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/words.py", line 57, in <module>
    walk(chain)
  File "/Users/mike/teaching/2017-04-24/words.py", line 51, in walk
    word = random.choice(chain[last])
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/random.py", line 275, in choice
    return seq[int(self.random() * len(seq))]  # raises IndexError if seq is empty
IndexError: list index out of range
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
while; and your water is a sore decayer of your whoreson dead body.
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
my lord? I heard thee speak me a speech once, but it was never acted; or, if it was, not above once; for the play, I remember, pleased not the million; 'twas caviare to the general: but it was--as I received it, and others, whose judgments in such matters cried in the top of mine--an excellent play, well digested in the scenes, set down with as much modesty as cunning.
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
my lord! Hillo, ho, ho, boy!
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
dearest foe in heaven Or ever I had seen that day, Horatio!
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
Madam, how like you this play?
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
will come straight. Look you lay home to him: Tell him his pranks have been too broad to bear with, And that your grace hath screen'd and stood between Much heat and him.
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
thousand natural shocks That flesh is heir to, 'tis a consummation Devoutly to be wish'd.
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
panders will.
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
solicitings, As they fell out by time, by means and place, All given to mine ear.
>>> 
>>> 
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
compulsatory, those foresaid lands So by his father, with all bonds of law, To our most valiant brother.
>>> chain['dead', 'and']
['gone,', 'gone;', "turn'd"]
>>> chain['dead', 'body.']
["Here's"]
>>> 
>>> 
>>> sum([len(set(words)) > 1 for words in chain.values()])
2197
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
the devil: and the cue for passion That I distrust you. 0
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
his meed he's unfellowed. 0.092657416389
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
region, so, Nor do not o'errule me it does he has imponed, as grace, As there is a-making, You have seen of great man dies. 0.302032142383
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
to her As to peace-parted souls. 0.0144155978843
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/words.py =============
are spent. Of him, sir. 0.00166417606303
>>> 
>>> 
>>> 
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/circuitous.py ===========
>>> 
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
>>> 
>>> c = Circle(10)

Traceback (most recent call last):
  File "<pyshell#1573>", line 1, in <module>
    c = Circle(10)
NameError: name 'Circle' is not defined
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
>>> Circle(10)
<circuitous.Circle instance at 0x101ea96c8>
>>> c = Circle(10)
>>> 
>>> c.area()
314.159
>>> c.circumference()
62.800000000000004
>>> 
