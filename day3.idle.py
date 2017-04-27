Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 12:39:47) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> # Python for Engineers, Part 2
>>> # Copyright (c) 2017 Raymond Hettinger
>>> 
>>> 
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/abstract.py ============
**********************************************************************
File "/Users/mike/teaching/2017-04-24/abstract.py", line 8, in __main__.SkipSeq
Failed example:
    skip = SkipSeq('abcdefg')
Exception raised:
    Traceback (most recent call last):
      File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/doctest.py", line 1315, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.SkipSeq[0]>", line 1, in <module>
        skip = SkipSeq('abcdefg')
    TypeError: this constructor takes no arguments
**********************************************************************
File "/Users/mike/teaching/2017-04-24/abstract.py", line 9, in __main__.SkipSeq
Failed example:
    skip[0]
Exception raised:
    Traceback (most recent call last):
      File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/doctest.py", line 1315, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.SkipSeq[1]>", line 1, in <module>
        skip[0]
    NameError: name 'skip' is not defined
**********************************************************************
File "/Users/mike/teaching/2017-04-24/abstract.py", line 11, in __main__.SkipSeq
Failed example:
    skip[1]
Exception raised:
    Traceback (most recent call last):
      File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/doctest.py", line 1315, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.SkipSeq[2]>", line 1, in <module>
        skip[1]
    NameError: name 'skip' is not defined
**********************************************************************
File "/Users/mike/teaching/2017-04-24/abstract.py", line 13, in __main__.SkipSeq
Failed example:
    len(skip)
Exception raised:
    Traceback (most recent call last):
      File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/doctest.py", line 1315, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.SkipSeq[3]>", line 1, in <module>
        len(skip)
    NameError: name 'skip' is not defined
**********************************************************************
1 items had failures:
   4 of   4 in __main__.SkipSeq
***Test Failed*** 4 failures.
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/abstract.py ============
**********************************************************************
File "/Users/mike/teaching/2017-04-24/abstract.py", line 9, in __main__.SkipSeq
Failed example:
    skip[0]
Exception raised:
    Traceback (most recent call last):
      File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/doctest.py", line 1315, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.SkipSeq[1]>", line 1, in <module>
        skip[0]
    AttributeError: SkipSeq instance has no attribute '__getitem__'
**********************************************************************
File "/Users/mike/teaching/2017-04-24/abstract.py", line 11, in __main__.SkipSeq
Failed example:
    skip[1]
Exception raised:
    Traceback (most recent call last):
      File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/doctest.py", line 1315, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.SkipSeq[2]>", line 1, in <module>
        skip[1]
    AttributeError: SkipSeq instance has no attribute '__getitem__'
**********************************************************************
File "/Users/mike/teaching/2017-04-24/abstract.py", line 13, in __main__.SkipSeq
Failed example:
    len(skip)
Exception raised:
    Traceback (most recent call last):
      File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/doctest.py", line 1315, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.SkipSeq[3]>", line 1, in <module>
        len(skip)
    AttributeError: SkipSeq instance has no attribute '__len__'
**********************************************************************
1 items had failures:
   3 of   4 in __main__.SkipSeq
***Test Failed*** 3 failures.
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/abstract.py ============
**********************************************************************
File "/Users/mike/teaching/2017-04-24/abstract.py", line 13, in __main__.SkipSeq
Failed example:
    len(skip)
Exception raised:
    Traceback (most recent call last):
      File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/doctest.py", line 1315, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.SkipSeq[3]>", line 1, in <module>
        len(skip)
    AttributeError: SkipSeq instance has no attribute '__len__'
**********************************************************************
1 items had failures:
   1 of   4 in __main__.SkipSeq
***Test Failed*** 1 failures.
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/abstract.py ============
**********************************************************************
File "/Users/mike/teaching/2017-04-24/abstract.py", line 13, in __main__.SkipSeq
Failed example:
    len(skip)
Expected:
    4
Got:
    3
**********************************************************************
1 items had failures:
   1 of   4 in __main__.SkipSeq
***Test Failed*** 1 failures.
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/abstract.py ============
>>> 
>>> 
>>> len(SkipSeq('ab'))
2
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/abstract.py ============
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/abstract.py ============
>>> 
>>> skip = SkipSeq('hello world')
>>> skip[0]
'h'
>>> skip[1]
'l'
>>> skip[2]
'o'
>>> len(skip)
6
>>> for c in skip:
	print c

	
h
l
o
w
r
d
>>> [c for c in skip]
['h', 'l', 'o', 'w', 'r', 'd']
>>> [c.upper() for c in skip]
['H', 'L', 'O', 'W', 'R', 'D']
>>> ''.join([c.upper() for c in skip])
'HLOWRD'
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/abstract.py ============
>>> skip = SkipSeq('hello world')
>>> skip.capitalize()
'HLOWRD'
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/abstract.py ============
>>> skip = SkipSeq('ALL YOUR BASE')
>>> skip.uncapitalize()
'alyu ae'
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/abstract.py ============
**********************************************************************
File "/Users/mike/teaching/2017-04-24/abstract.py", line 36, in __main__.SkipTwoSeq
Failed example:
    skip = SkipTwoSeq('abcdefg')
Exception raised:
    Traceback (most recent call last):
      File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/doctest.py", line 1315, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.SkipTwoSeq[0]>", line 1, in <module>
        skip = SkipTwoSeq('abcdefg')
    TypeError: this constructor takes no arguments
**********************************************************************
File "/Users/mike/teaching/2017-04-24/abstract.py", line 37, in __main__.SkipTwoSeq
Failed example:
    skip[0]
Exception raised:
    Traceback (most recent call last):
      File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/doctest.py", line 1315, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.SkipTwoSeq[1]>", line 1, in <module>
        skip[0]
    NameError: name 'skip' is not defined
**********************************************************************
File "/Users/mike/teaching/2017-04-24/abstract.py", line 39, in __main__.SkipTwoSeq
Failed example:
    skip[1]
Exception raised:
    Traceback (most recent call last):
      File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/doctest.py", line 1315, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.SkipTwoSeq[2]>", line 1, in <module>
        skip[1]
    NameError: name 'skip' is not defined
**********************************************************************
File "/Users/mike/teaching/2017-04-24/abstract.py", line 41, in __main__.SkipTwoSeq
Failed example:
    len(skip)
Exception raised:
    Traceback (most recent call last):
      File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/doctest.py", line 1315, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.SkipTwoSeq[3]>", line 1, in <module>
        len(skip)
    NameError: name 'skip' is not defined
**********************************************************************
1 items had failures:
   4 of   4 in __main__.SkipTwoSeq
***Test Failed*** 4 failures.
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/abstract.py ============
**********************************************************************
File "/Users/mike/teaching/2017-04-24/abstract.py", line 37, in __main__.SkipTwoSeq
Failed example:
    skip[0]
Exception raised:
    Traceback (most recent call last):
      File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/doctest.py", line 1315, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.SkipTwoSeq[1]>", line 1, in <module>
        skip[0]
    AttributeError: SkipTwoSeq instance has no attribute '__getitem__'
**********************************************************************
File "/Users/mike/teaching/2017-04-24/abstract.py", line 39, in __main__.SkipTwoSeq
Failed example:
    skip[1]
Exception raised:
    Traceback (most recent call last):
      File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/doctest.py", line 1315, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.SkipTwoSeq[2]>", line 1, in <module>
        skip[1]
    AttributeError: SkipTwoSeq instance has no attribute '__getitem__'
**********************************************************************
File "/Users/mike/teaching/2017-04-24/abstract.py", line 41, in __main__.SkipTwoSeq
Failed example:
    len(skip)
Exception raised:
    Traceback (most recent call last):
      File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/doctest.py", line 1315, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.SkipTwoSeq[3]>", line 1, in <module>
        len(skip)
    AttributeError: SkipTwoSeq instance has no attribute '__len__'
**********************************************************************
1 items had failures:
   3 of   4 in __main__.SkipTwoSeq
***Test Failed*** 3 failures.
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/abstract.py ============
**********************************************************************
File "/Users/mike/teaching/2017-04-24/abstract.py", line 41, in __main__.SkipTwoSeq
Failed example:
    len(skip)
Exception raised:
    Traceback (most recent call last):
      File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/doctest.py", line 1315, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.SkipTwoSeq[3]>", line 1, in <module>
        len(skip)
    AttributeError: SkipTwoSeq instance has no attribute '__len__'
**********************************************************************
1 items had failures:
   1 of   4 in __main__.SkipTwoSeq
***Test Failed*** 1 failures.
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/abstract.py ============
**********************************************************************
File "/Users/mike/teaching/2017-04-24/abstract.py", line 41, in __main__.SkipTwoSeq
Failed example:
    len(skip)
Expected:
    3
Got:
    2
**********************************************************************
1 items had failures:
   1 of   4 in __main__.SkipTwoSeq
***Test Failed*** 1 failures.
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/abstract.py ============
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/abstract.py ============
>>> 
>>> skip = SkipTwoSeq('hello world')
>>> skip[0]
'h'
>>> for c in skip:
	print c

	
h
l
w
l
>>> [c.upper() for c in skip]
['H', 'L', 'W', 'L']
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/abstract.py ============
>>> skip = SkipTwoSeq('hello world')
>>> skip.capitalize()
'HLWL'
>>> skip = SkipTwoSeq('ALL YOUR BASE')
>>> skip.uncapitalize()
'a ube'
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/abstract.py ============
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/abstract.py ============
>>> 
>>> SkipSeq.__bases__
(<class '__main__.Capper'>, <class '__main__.Uncapper'>)
>>> SkipSeq.mro()
[<class '__main__.SkipSeq'>, <class '__main__.Capper'>, <class '__main__.Uncapper'>, <type 'object'>]
>>> help(SkipSeq)
Help on class SkipSeq in module __main__:

class SkipSeq(Capper, Uncapper)
 |  A sequence that skips every other element.
 |  
 |      >>> skip = SkipSeq('abcdefg')
 |      >>> skip[0]
 |      'a'
 |      >>> skip[1]
 |      'c'
 |      >>> len(skip)
 |      4
 |  
 |  Method resolution order:
 |      SkipSeq
 |      Capper
 |      Uncapper
 |      __builtin__.object
 |  
 |  Methods defined here:
 |  
 |  __getitem__(self, index)
 |  
 |  __init__(self, sequence)
 |  
 |  __len__(self)
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from Capper:
 |  
 |  capitalize(self)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Capper:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from Uncapper:
 |  
 |  uncapitalize(self)

>>> 
>>> 
>>> 
>>> skip = SkipTwoSeq('ALL YOUR BASE')
>>> skip.uncapper()

Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    skip.uncapper()
AttributeError: 'SkipTwoSeq' object has no attribute 'uncapper'
>>> skip.uncapitalize()
'a ube'
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/abstract.py ============
>>> 
>>> Capper()
<__main__.Capper object at 0x10310bc10>
>>> cap = Capper()
>>> cap.capitalize()

Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    cap.capitalize()
  File "/Users/mike/teaching/2017-04-24/abstract.py", line 9, in capitalize
    return ''.join([c.upper() for c in self])
TypeError: 'Capper' object is not iterable
>>> 
>>> 
>>> 
>>> class Jumper:
	def jump(self):
		print 'boing!'

		
>>> class Swimmer:
	def swim(self):
		print 'splash'

		
>>> class Shooter:
	def shoot(self):
		print 'pow!'

		
>>> class PistolRabbit(Jumper, Shooter):
	def draw(self):
		print 'animate'

		
>>> class LaserShark(Swimmer, Shooter):
	def draw(self):
		print 'animate'

		
>>> Jumper()
<__main__.Jumper instance at 0x102fa86c8>
>>> 
>>> 
>>> cap = Capper()
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> cap.capitalize()

Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    cap.capitalize()
  File "/Users/mike/teaching/2017-04-24/abstract.py", line 9, in capitalize
    Mixins are also TERRIBLE :-(
TypeError: 'Capper' object is not iterable
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/abstract.py ============
>>> cap.capitalize()

Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    cap.capitalize()
NameError: name 'cap' is not defined
>>> cap = Capper()
>>> cap.capitalize()

Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    cap.capitalize()
  File "/Users/mike/teaching/2017-04-24/abstract.py", line 17, in capitalize
    return ''.join([c.upper() for c in self])
TypeError: 'Capper' object is not iterable
>>> 
>>> 
>>> 
>>> cap = Capper()
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> cap.capitalize()

Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    cap.capitalize()
  File "/Users/mike/teaching/2017-04-24/abstract.py", line 17, in capitalize
    return ''.join([c.upper() for c in self])
TypeError: 'Capper' object is not iterable
>>> 
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/abstract.py ============
>>> 
>>> 
>>> class Foo(Capper):
	pass

>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/abstract.py ============
>>> Capper()

Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    Capper()
TypeError: Can't instantiate abstract class Capper with abstract methods __getitem__, __len__
>>> 
>>> 
>>> class Foo(Capper):
	pass

>>> Foo()

Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    Foo()
TypeError: Can't instantiate abstract class Foo with abstract methods __getitem__, __len__
>>> 
>>> 
>>> class Foo(Capper):
	def __getitem__(self, index):
		return index

	
>>> Foo()

Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    Foo()
TypeError: Can't instantiate abstract class Foo with abstract methods __len__
>>> 
>>> 
>>> import inspect
>>> 
>>> 
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/abstract.py ============
>>> Uncapper()

Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    Uncapper()
TypeError: Can't instantiate abstract class Uncapper with abstract methods __getitem__, __len__
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/abstract.py ============
>>> 
>>> skip = SkipTwoSeq('ALL YOUR BASE')
>>> skip = SkipSeq('ALL YOUR BASE')
>>> 
>>> 
>>> skip = SkipSeq('hello world')
>>> skip.count('l')
1
>>> skip.capitalize()
'HLOWRD'
>>> skip.mro()

Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    skip.mro()
AttributeError: 'SkipSeq' object has no attribute 'mro'
>>> SkipSeq.mro()
[<class '__main__.SkipSeq'>, <class '__main__.Capper'>, <class '__main__.Uncapper'>, <class '_abcoll.Sequence'>, <class '_abcoll.Sized'>, <class '_abcoll.Iterable'>, <class '_abcoll.Container'>, <type 'object'>]
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/filedict.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/filedict.py", line 26, in <module>
    d = FileDict('starwars')
TypeError: object() takes no parameters
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/filedict.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/filedict.py", line 29, in <module>
    d = FileDict('starwars')
TypeError: Can't instantiate abstract class FileDict with abstract methods __delitem__, __getitem__, __iter__, __len__, __setitem__
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/filedict.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/filedict.py", line 34, in <module>
    d = FileDict('starwars')
TypeError: Can't instantiate abstract class FileDict with abstract methods __getitem__, __iter__, __len__, __setitem__
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/filedict.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/filedict.py", line 34, in <module>
    d = FileDict('starwars')
TypeError: Can't instantiate abstract class FileDict with abstract methods __getitem__, __iter__, __len__, __setitem__
>>> 
>>> 
>>> str.strip
<method 'strip' of 'str' objects>
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/filedict.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/filedict.py", line 39, in <module>
    d = FileDict('starwars')
TypeError: Can't instantiate abstract class FileDict with abstract methods __iter__, __len__, __setitem__
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/filedict.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/filedict.py", line 44, in <module>
    d = FileDict('starwars')
TypeError: Can't instantiate abstract class FileDict with abstract methods __iter__, __len__
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/filedict.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/filedict.py", line 47, in <module>
    d = FileDict('starwars')
TypeError: Can't instantiate abstract class FileDict with abstract methods __iter__
>>> 
>>> 
>>> 
>>> iter({'a': 1, 'b': 2})
<dictionary-keyiterator object at 0x10275f1b0>
>>> it = iter({'a': 1, 'b': 2})
>>> it
<dictionary-keyiterator object at 0x10275f208>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)

Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    next(it)
StopIteration
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/filedict.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/filedict.py", line 51, in <module>
    d['hero'] = 'Luke'
  File "/Users/mike/teaching/2017-04-24/filedict.py", line 40, in __setitem__
    with open(filepath, 'w') as f:
IOError: [Errno 2] No such file or directory: 'starwars/hero'
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/filedict.py ============
<__main__.FileDict object at 0x103861b10>

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/filedict.py", line 57, in <module>
    d['hero'] = ('Rey', 'Finn')
  File "/Users/mike/teaching/2017-04-24/filedict.py", line 42, in __setitem__
    f.write(value)
TypeError: expected a string or other character buffer object
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/filedict.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/filedict.py", line 51, in <module>
    d = FileDict('starwars')
  File "/Users/mike/teaching/2017-04-24/filedict.py", line 28, in __init__
    os.mkdir(folder)
OSError: [Errno 17] File exists: 'starwars'
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/filedict.py ============
<__main__.FileDict object at 0x10384ead0>
['hero']
["('Rey', 'Finn')"]
>>> 
>>> 
>>> import errno
>>> for name in dir(errno):
	if getattr(errno, name) == 17
	
SyntaxError: invalid syntax
>>> for name in dir(errno):
	if getattr(errno, name) == 17:
		print name

		
EEXIST
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/filedict.py ============
<__main__.FileDict object at 0x10274ead0>
['hero']
["('Rey', 'Finn')"]
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/filedict.py ============
<__main__.FileDict object at 0x10274ead0>
['hero']
["('Rey', 'Finn')"]
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/filedict.py ============
<__main__.FileDict object at 0x10384ead0>
['hero']
["('Rey', 'Finn')"]
>>> 
>>> d
<__main__.FileDict object at 0x10384ead0>
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/filedict.py ============
FileDict('starwars', [('hero', "'Luke'"), ('villain', "'Darth Vader'")])
['hero']
["('Rey', 'Finn')"]
>>> 
>>> 
>>> 'hero' in d
True
>>> 
>>> FileDict('starwars', [('hero', "'Luke'"), ('villain', "'Darth Vader'")])

Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    FileDict('starwars', [('hero', "'Luke'"), ('villain', "'Darth Vader'")])
TypeError: __init__() takes exactly 2 arguments (3 given)
>>> 
>>> dict([])
{}
>>> dict({})
{}
>>> dict(a=1)
{'a': 1}
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/filedict.py ============
FileDict('starwars', [('hero', "'Luke'"), ('villain', "'Darth Vader'")])
['hero']
["('Rey', 'Finn')"]
>>> FileDict('starwars', [('hero', "'Luke'"), ('villain', "'Darth Vader'")])
FileDict('starwars', [('hero', '"\'Luke\'"'), ('villain', '"\'Darth Vader\'"')])
>>> FileDict('starwars', [('hero', "'Luke'"), ('villain', "'Darth Vader'")])
FileDict('starwars', [('hero', '"\'Luke\'"'), ('villain', '"\'Darth Vader\'"')])
>>> FileDict('starwars', [('hero', "'Luke'"), ('villain', "'Darth Vader'")])
FileDict('starwars', [('hero', '"\'Luke\'"'), ('villain', '"\'Darth Vader\'"')])
>>> 
>>> d['hero']
'"\'Luke\'"'
>>> d['hero'] = d['hero']
>>> d['hero']
'\'"\\\'Luke\\\'"\''
>>> d['hero'] = d['hero']
>>> d['hero']
'\'\\\'"\\\\\\\'Luke\\\\\\\'"\\\'\''
>>> d['hero'] = d['hero']
>>> d['hero']
'\'\\\'\\\\\\\'"\\\\\\\\\\\\\\\'Luke\\\\\\\\\\\\\\\'"\\\\\\\'\\\'\''
>>> 
>>> 
>>> d['number'] = 5
>>> d['number']
'5'
>>> 
>>> 
>>> # REPL: Read Eval Print Loop
>>> # aka Python prompt
>>> # aka Python shell
>>> 
>>> s = '5'
>>> eval(s)
5
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/filedict.py ============
FileDict('starwars', [('hero', 'Luke'), ('number', 5), ('villain', 'Darth Vader')])
['hero', 'number']
[('Rey', 'Finn'), 5]
>>> 
>>> 
>>> d['hello'] = 'world'
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/filedict.py ============
FileDict('starwars', [('hello', 'world'), ('hero', 'Luke'), ('number', 5), ('villain', 'Darth Vader')])
['hello', 'hero', 'number']
['world', ('Rey', 'Finn'), 5]
>>> 
>>> 
>>> 
>>> int
<type 'int'>
>>> d['type'] = int
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/filedict.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/filedict.py", line 65, in <module>
    print d
  File "/Users/mike/teaching/2017-04-24/filedict.py", line 39, in __repr__
    self.items())
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/_abcoll.py", line 414, in items
    return [(key, self[key]) for key in self]
  File "/Users/mike/teaching/2017-04-24/filedict.py", line 48, in __getitem__
    return eval(f.read())
  File "<string>", line 1
    <type 'int'>
    ^
SyntaxError: invalid syntax
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/filedict.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/filedict.py", line 65, in <module>
    print d
  File "/Users/mike/teaching/2017-04-24/filedict.py", line 39, in __repr__
    self.items())
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/_abcoll.py", line 414, in items
    return [(key, self[key]) for key in self]
  File "/Users/mike/teaching/2017-04-24/filedict.py", line 48, in __getitem__
    return pickle.load(f)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/pickle.py", line 1384, in load
    return Unpickler(file).load()
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/pickle.py", line 864, in load
    dispatch[key](self)
KeyError: "'"
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/filedict.py ============
FileDict('starwars', [('hero', 'Luke'), ('villain', 'Darth Vader')])
['hero']
[('Rey', 'Finn')]
>>> 
>>> 
>>> d['func'] = len
>>> d['func']
<built-in function len>
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/filedict.py ============
FileDict('starwars', [('func', <built-in function len>), ('hero', 'Luke'), ('villain', 'Darth Vader')])
['func', 'hero']
[<built-in function len>, ('Rey', 'Finn')]
>>> FileDict('starwars', [('func', <built-in function len>), ('hero', 'Luke'), ('villain', 'Darth Vader')])
SyntaxError: invalid syntax
>>> 
>>> 
>>> del d['func']
>>> d
FileDict('starwars', [('hero', ('Rey', 'Finn'))])
>>> FileDict('starwars', [('hero', ('Rey', 'Finn'))])
FileDict('starwars', [('hero', ('Rey', 'Finn'))])
>>> 
>>> 
>>> del d['z']

Traceback (most recent call last):
  File "<pyshell#216>", line 1, in <module>
    del d['z']
  File "/Users/mike/teaching/2017-04-24/filedict.py", line 43, in __delitem__
    os.remove(filepath)
OSError: [Errno 2] No such file or directory: 'starwars/z'
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/filedict.py ============
FileDict('starwars', [('hero', 'Luke'), ('villain', 'Darth Vader')])
['hero']
[('Rey', 'Finn')]
>>> del d['z']

Traceback (most recent call last):
  File "<pyshell#217>", line 1, in <module>
    del d['z']
  File "/Users/mike/teaching/2017-04-24/filedict.py", line 46, in __delitem__
    raise KeyError(key)
KeyError: 'z'
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/filedict.py ============
FileDict('starwars', [('hero', 'Luke'), ('villain', 'Darth Vader')])
['hero']
[('Rey', 'Finn')]
>>> d['z']

Traceback (most recent call last):
  File "<pyshell#218>", line 1, in <module>
    d['z']
  File "/Users/mike/teaching/2017-04-24/filedict.py", line 50, in __getitem__
    with open(filepath) as f:
IOError: [Errno 2] No such file or directory: 'starwars/z'
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/filedict.py ============
FileDict('starwars', [('hero', 'Luke'), ('villain', 'Darth Vader')])
['hero']
[('Rey', 'Finn')]
>>> 
>>> 
>>> d['z']

Traceback (most recent call last):
  File "<pyshell#221>", line 1, in <module>
    d['z']
  File "/Users/mike/teaching/2017-04-24/filedict.py", line 54, in __getitem__
    raise KeyError(key)
KeyError: 'z'
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/filedict.py ============
FileDict('starwars', [('hero', 'Luke'), ('villain', 'Darth Vader')])
['hero']
[('Rey', 'Finn')]
>>> 
>>> 
>>> # lunch until 1:20pm
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/filedict.py ============
FileDict('starwars', [('hero', 'Luke'), ('villain', 'Darth Vader')])
['hero']
[('Rey', 'Finn')]
>>> 
>>> d[5] = 'hello'

Traceback (most recent call last):
  File "<pyshell#226>", line 1, in <module>
    d[5] = 'hello'
  File "/Users/mike/teaching/2017-04-24/filedict.py", line 60, in __setitem__
    filepath = os.path.join(self.folder, key)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/posixpath.py", line 68, in join
    if b.startswith('/'):
AttributeError: 'int' object has no attribute 'startswith'
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/filedict.py ============
FileDict('starwars', [('hero', 'Luke'), ('villain', 'Darth Vader')])
['hero']
[('Rey', 'Finn')]
>>> d[5] = 'hello'

Traceback (most recent call last):
  File "<pyshell#227>", line 1, in <module>
    d[5] = 'hello'
  File "/Users/mike/teaching/2017-04-24/filedict.py", line 60, in __setitem__
    raise TypeError('FileDict keys must be strings')
TypeError: FileDict keys must be strings
>>> 
>>> d[':'] = 'hello'
>>> d
FileDict('starwars', [(':', 'hello'), ('hero', ('Rey', 'Finn'))])
>>> del d[':']
>>> d
FileDict('starwars', [('hero', ('Rey', 'Finn'))])
>>> 
>>> d[str(range(256))] = 'too long'

Traceback (most recent call last):
  File "<pyshell#234>", line 1, in <module>
    d[str(range(256))] = 'too long'
  File "/Users/mike/teaching/2017-04-24/filedict.py", line 61, in __setitem__
    with open(filepath, 'w') as f:
IOError: [Errno 63] File name too long: 'starwars/[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255]'
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/sqldict.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/sqldict.py", line 23, in <module>
    d = SqlDict('starwars.db')
TypeError: object() takes no parameters
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/sqldict.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/sqldict.py", line 23, in <module>
    d = SqlDict('starwars.db')
TypeError: object() takes no parameters
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/sqldict.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/sqldict.py", line 26, in <module>
    d = SqlDict('starwars.db')
TypeError: Can't instantiate abstract class SqlDict with abstract methods __delitem__, __getitem__, __iter__, __len__, __setitem__
>>> 
>>> 
>>> "fluent PHP"
'fluent PHP'
>>> 
>>> 
>>> 
>>> list.append
<method 'append' of 'list' objects>
>>> 
>>> [5].append(1)
>>> [5] + [1]
[5, 1]
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/sqldict.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/sqldict.py", line 35, in <module>
    d = SqlDict('starwars.db')
TypeError: Can't instantiate abstract class SqlDict with abstract methods __delitem__, __iter__, __len__, __setitem__
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/sqldict.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/sqldict.py", line 37, in <module>
    d = SqlDict('starwars.db')
TypeError: Can't instantiate abstract class SqlDict with abstract methods __delitem__, __iter__, __len__, __setitem__
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/sqldict.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/sqldict.py", line 35, in <module>
    d = SqlDict('starwars.db')
TypeError: Can't instantiate abstract class SqlDict with abstract methods __delitem__, __iter__, __len__, __setitem__
>>> 
>>> 
>>> 
>>> 
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/sqldict.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/sqldict.py", line 35, in <module>
    d = SqlDict('starwars.db')
TypeError: Can't instantiate abstract class SqlDict with abstract methods __delitem__, __iter__, __len__, __setitem__
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/sqldict.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/sqldict.py", line 40, in <module>
    d = SqlDict('starwars.db')
TypeError: Can't instantiate abstract class SqlDict with abstract methods __delitem__, __iter__, __len__
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/sqldict.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/sqldict.py", line 47, in <module>
    d = SqlDict('starwars.db')
TypeError: Can't instantiate abstract class SqlDict with abstract methods __iter__, __len__
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/sqldict.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/sqldict.py", line 67, in <module>
    d['hero'] = 'Luke'
  File "/Users/mike/teaching/2017-04-24/sqldict.py", line 35, in __setitem__
    if key in self:   # LBYL creates a race condition
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/_abcoll.py", line 388, in __contains__
    self[key]
  File "/Users/mike/teaching/2017-04-24/sqldict.py", line 32, in __getitem__
    return row[0]
TypeError: 'NoneType' object has no attribute '__getitem__'
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/sqldict.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/sqldict.py", line 68, in <module>
    d = SqlDict('starwars.db')
  File "/Users/mike/teaching/2017-04-24/sqldict.py", line 25, in __init__
    c.execute('CREATE TABLE Dict (key text, value text)')
OperationalError: table Dict already exists
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/sqldict.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/sqldict.py", line 68, in <module>
    d = SqlDict('starwars.db')
  File "/Users/mike/teaching/2017-04-24/sqldict.py", line 25, in __init__
    c.execute('CREATE TABLE Dict (key text, value text)')
OperationalError: table Dict already exists
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/sqldict.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/sqldict.py", line 71, in <module>
    d = SqlDict('starwars.db')
  File "/Users/mike/teaching/2017-04-24/sqldict.py", line 28, in __init__
    except OperationalError:
NameError: global name 'OperationalError' is not defined
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/sqldict.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/sqldict.py", line 71, in <module>
    d = SqlDict('starwars.db')
  File "/Users/mike/teaching/2017-04-24/sqldict.py", line 28, in __init__
    except OperationalError:
NameError: global name 'OperationalError' is not defined
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/sqldict.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/sqldict.py", line 72, in <module>
    d['hero'] = 'Luke'
  File "/Users/mike/teaching/2017-04-24/sqldict.py", line 43, in __setitem__
    c.execute('INSERT INTO Dict (?, ?)', (key, value))
OperationalError: near "?": syntax error
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/sqldict.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/sqldict.py", line 72, in <module>
    d['hero'] = 'Luke'
  File "/Users/mike/teaching/2017-04-24/sqldict.py", line 43, in __setitem__
    c.execute('INSERT INTO Dict (?, ?)', (key, value))
OperationalError: near "?": syntax error
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/sqldict.py ============
<__main__.SqlDict object at 0x103871d10>

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/sqldict.py", line 77, in <module>
    d['hero'] = ('Rey', 'Finn')
  File "/Users/mike/teaching/2017-04-24/sqldict.py", line 43, in __setitem__
    c.execute('INSERT INTO Dict VALUES (?, ?)', (key, value))
InterfaceError: Error binding parameter 1 - probably unsupported type.
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/sqldict.py ============
<__main__.SqlDict object at 0x10285ed10>
<__main__.SqlDict object at 0x10285ed10>
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/sqldict.py ============
<__main__.SqlDict object at 0x1030f1d10>
<__main__.SqlDict object at 0x1030f1d10>
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/sqldict.py ============
SqlDict('starwars.db', [(u'hero', u'Luke'), (u'villain', u'Darth')])
SqlDict('starwars.db', [(u'hero', [u'Rey', u'Finn'])])
>>> SqlDict('starwars.db', [(u'hero', [u'Rey', u'Finn'])])

Traceback (most recent call last):
  File "<pyshell#249>", line 1, in <module>
    SqlDict('starwars.db', [(u'hero', [u'Rey', u'Finn'])])
TypeError: __init__() takes exactly 2 arguments (3 given)
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/sqldict.py ============
SqlDict('starwars.db', [(u'hero', u'Luke'), (u'villain', u'Darth')])
SqlDict('starwars.db', [(u'hero', [u'Rey', u'Finn'])])
>>> SqlDict('starwars.db', [(u'hero', [u'Rey', u'Finn'])])
SqlDict('starwars.db', [(u'hero', [u'Rey', u'Finn'])])
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/sqldict.py ============
SqlDict('starwars.db', [(u'hero', u'Luke'), (u'villain', u'Darth')])
SqlDict('starwars.db', [(u'hero', [u'Rey', u'Finn'])])
>>> del d['z']

Traceback (most recent call last):
  File "<pyshell#251>", line 1, in <module>
    del d['z']
  File "/Users/mike/teaching/2017-04-24/sqldict.py", line 55, in __delitem__
    raise KeyError(key)
KeyError: 'z'
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/sqldict.py ============
SqlDict('starwars.db', [(u'hero', u'Luke'), (u'villain', u'Darth')])
SqlDict('starwars.db', [(u'hero', [u'Rey', u'Finn'])])
>>> 
>>> 
>>> it = iter(d)
>>> it
<generator object __iter__ at 0x1030eb0f0>
>>> next(it)
u'5'
>>> next(it)
u'hero'
>>> next(it)

Traceback (most recent call last):
  File "<pyshell#258>", line 1, in <module>
    next(it)
StopIteration
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/sqldict.py ============
SqlDict('starwars.db', [(u'5', 3), (u'hero', u'Luke'), (u'villain', u'Darth')])
SqlDict('starwars.db', [(u'5', 3), (u'hero', [u'Rey', u'Finn'])])
>>> d.copy()

Traceback (most recent call last):
  File "<pyshell#259>", line 1, in <module>
    d.copy()
  File "/Users/mike/teaching/2017-04-24/sqldict.py", line 83, in copy
    'Duplicate copies of a SqlDict share the same data')
NotImplementedError: Duplicate copies of a SqlDict share the same data
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/sqldict.py ============
SqlDict('starwars.db', [(u'5', 3), (u'hero', u'Luke'), (u'villain', u'Darth')])
SqlDict('starwars.db', [(u'5', 3), (u'hero', [u'Rey', u'Finn'])])
>>> 
>>> 
>>> d['hero']

Traceback (most recent call last):
  File "<pyshell#262>", line 1, in <module>
    d['hero']
  File "/Users/mike/teaching/2017-04-24/sqldict.py", line 38, in __getitem__
    c = self.connection.cursor()
ProgrammingError: Cannot operate on a closed database.
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/test_docfinder.py", line 19, in <module>
    print list(normalize(['Hettinger', 'enumerates', 'AND']))
TypeError: 'NoneType' object is not iterable
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/test_docfinder.py", line 19, in <module>
    print list(normalize(['Hettinger', 'enumerates', 'AND']))
TypeError: 'NoneType' object is not iterable
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/test_docfinder.py", line 19, in <module>
    print list(normalize(['Hettinger', 'enumerates', 'AND']))
TypeError: 'NoneType' object is not iterable
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/test_docfinder.py", line 19, in <module>
    print list(normalize(['Hettinger', 'enumerates', 'AND']))
TypeError: 'NoneType' object is not iterable
>>> 
>>> 'hiss'.rstrip('s')
'hi'
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
[]
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
['hettinger', 'enumerate']
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
['hettinger', 'enumerate']
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/test_docfinder.py", line 25, in <module>
    with open(fullname) as f:
IOError: [Errno 2] No such file or directory: 'data/peps/pep-0238.txt'
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/test_docfinder.py", line 27, in <module>
    for term, score in score_document(text, n=10):
TypeError: 'NoneType' object is not iterable
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/test_docfinder.py", line 27, in <module>
    for term, score in score_document(text, n=10):
TypeError: 'NoneType' object is not iterable
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
a 0.043229497775
division 0.0305149396058
to 0.0298792116974
i 0.0228862047044
for 0.020979020979
in 0.018118245391
that 0.0152574698029
python 0.013986013986
be 0.0133502860776
true 0.0123966942149
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/test_docfinder.py", line 32, in <module>
    create_db(force=False)
  File "/Users/mike/teaching/2017-04-24/docfinder.py", line 87, in create_db
    c.execute('CREATE TABLE Document (uri text, content blob)')
OperationalError: table Document already exists
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
pep-0237 14330
pep-0236 13914
pep-0235 6657
>>> 
>>> 
>>> import bz2
>>> help(bz2.compress)
Help on built-in function compress in module bz2:

compress(...)
    compress(data [, compresslevel=9]) -> string
    
    Compress data in one shot. If you want to compress data sequentially,
    use an instance of BZ2Compressor instead. The compresslevel parameter, if
    given, must be a number between 1 and 9.

>>> 
>>> dir(bz2)
['BZ2Compressor', 'BZ2Decompressor', 'BZ2File', '__author__', '__doc__', '__file__', '__name__', '__package__', 'compress', 'decompress']
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
pep-0237 14330

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/test_docfinder.py", line 43, in <module>
    add_document(uri, text)
  File "/Users/mike/teaching/2017-04-24/docfinder.py", line 99, in add_document
    c.execute('INSERT INTO Document VALUES (?, ?)', (uri, blob))
ProgrammingError: You must not use 8-bit bytestrings unless you use a text_factory that can interpret 8-bit bytestrings (like text_factory = str). It is highly recommended that you instead just switch your application to Unicode strings.
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/docfinder.py ===========
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
pep-0237 14330
pep-0236 13914
pep-0235 6657
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
pep-0237 14330
pep-0236 13914
pep-0235 6657
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
pep-0237 14330

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/test_docfinder.py", line 43, in <module>
    add_document(uri, text)
  File "/Users/mike/teaching/2017-04-24/docfinder.py", line 99, in add_document
    c.execute('INSERT INTO Document VALUES (?, ?)', (uri, blob))
IntegrityError: UNIQUE constraint failed: Document.uri
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
pep-0237 14330

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/test_docfinder.py", line 43, in <module>
    add_document(uri, text)
  File "/Users/mike/teaching/2017-04-24/docfinder.py", line 102, in add_document
    raise DuplicateURI(uri)
DuplicateURI: pep-0237
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
pep-0237 14330

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/test_docfinder.py", line 43, in <module>
    add_document(uri, text)
  File "/Users/mike/teaching/2017-04-24/docfinder.py", line 102, in add_document
    raise DuplicateURI(uri)
DuplicateURI: pep-0237
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
pep-0237 14330
pep-0236 13914
pep-0235 6657
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
pep-0001 21093
pep-0002 8338
pep-0003 2233
pep-0004 10523
pep-0005 3099
pep-0006 8439
pep-0007 6840
pep-0008 32509
pep-0009 9011
pep-0010 1989
pep-0011 6259
pep-0012 22407
pep-0020 1537
pep-0042 11386
pep-0100 42745
pep-0101 25522
pep-0102 20843
pep-0160 2253
pep-0200 14252
pep-0201 9674
pep-0202 2276
pep-0203 14147
pep-0204 11030
pep-0205 20340
pep-0206 3256
pep-0207 18802
pep-0208 10099
pep-0209 29438
pep-0210 298
pep-0211 6783
pep-0212 4902
pep-0213 8536
pep-0214 13522
pep-0215 4804
pep-0216 5438
pep-0217 1720
pep-0218 8029
pep-0219 8520
pep-0220 745
pep-0221 3978
pep-0222 8830
pep-0223 7504
pep-0224 8866
pep-0225 29809
pep-0226 4469
pep-0227 21474
pep-0228 4663
pep-0229 4214
pep-0230 14446
pep-0231 21675
pep-0232 8003
pep-0233 3051
pep-0234 20856
pep-0235 6657
pep-0236 13914
pep-0237 14330
pep-0238 23422
pep-0239 4782
pep-0240 3077
pep-0241 7703
pep-0242 8974
pep-0243 6702
pep-0244 6335
pep-0245 18731
pep-0246 32205
pep-0247 6400
pep-0248 12098
pep-0249 45244
pep-0250 5401
pep-0251 2560
pep-0252 32627
pep-0253 43135
pep-0254 651
pep-0255 20503
pep-0256 10434
pep-0257 11682
pep-0258 35850
pep-0259 3935
pep-0260 2283
pep-0261 10423
pep-0262 12859
pep-0263 8558
pep-0264 4868
pep-0265 7316
pep-0266 19657
pep-0267 10680
pep-0268 8856
pep-0269 7196
pep-0270 2369
pep-0271 1592
pep-0272 9070
pep-0273 8663
pep-0274 5133
pep-0275 12309
pep-0276 16273
pep-0277 4382
pep-0278 9188
pep-0279 8764
pep-0280 19835
pep-0281 4341
pep-0282 22943
pep-0283 11335
pep-0284 10687
pep-0285 17004
pep-0286 3568
pep-0287 32544
pep-0288 5529
pep-0289 10641
pep-0290 13748
pep-0291 6138
pep-0292 8200
pep-0293 15988
pep-0294 3085
pep-0295 3142
pep-0296 16807
pep-0297 3649
pep-0298 8767
pep-0299 3508
pep-0301 14086
pep-0302 28402
pep-0303 7489
pep-0304 13573
pep-0305 14881
pep-0306 3303
pep-0307 34989
pep-0308 17468
pep-0309 10100
pep-0310 8309
pep-0311 9588
pep-0312 5894
pep-0313 4621
pep-0314 9597
pep-0315 4024
pep-0316 15048
pep-0317 14865
pep-0318 30935
pep-0319 15878
pep-0320 6898
pep-0321 4359
pep-0322 5836
pep-0323 19812
pep-0324 18933
pep-0325 10752
pep-0326 20788
pep-0327 40620
pep-0328 10696
pep-0329 9942
pep-0330 9059
pep-0331 8047
pep-0332 2404
pep-0333 75600
pep-0334 13247
pep-0335 17286
pep-0336 2984
pep-0337 5020
pep-0338 13713
pep-0339 22727
pep-0340 22880
pep-0341 3006
pep-0342 26155
pep-0343 37815
pep-0344 21542
pep-0345 16422
pep-0346 44697
pep-0347 10942
pep-0348 19558
pep-0349 5267
pep-0350 25013
pep-0351 5073
pep-0352 11284
pep-0353 9578
pep-0354 8006
pep-0355 20431
pep-0356 5616
pep-0357 8522
pep-0358 10677
pep-0359 18232
pep-0360 3816
pep-0361 8888
pep-0362 12998
pep-0363 8679
pep-0364 10558
pep-0365 4860
pep-0366 5844
pep-0367 19947
pep-0368 34446
pep-0369 8871
pep-0370 8005
pep-0371 17421
pep-0372 12222
pep-0373 1543
pep-0374 54373
pep-0375 1700
pep-0376 23345
pep-0377 9724
pep-0378 9287
pep-0379 5247
pep-0380 17451
pep-0381 11665
pep-0382 8818
pep-0383 8230
pep-0384 13889
pep-0385 19368
pep-0386 18562
pep-0387 4226
pep-0389 12816
pep-0390 7822
pep-0391 27221
pep-0392 1879
pep-0393 18819
pep-0394 9999
pep-0395 11398
pep-0396 10635
pep-0397 18326
pep-0398 2432
pep-0399 8384
pep-0400 11410
pep-0401 4293
pep-0402 28759
pep-0403 10589
pep-0404 27552
pep-0444 70029
pep-0628 3599
pep-0666 4324
pep-0754 6401
pep-3000 6080
pep-3001 4576
pep-3002 4692
pep-3003 5988
pep-3099 7751
pep-3100 17744
pep-3101 34990
pep-3102 6903
pep-3103 25030
pep-3104 21700
pep-3105 4855
pep-3106 11245
pep-3107 11028
pep-3108 30384
pep-3109 7740
pep-3110 8554
pep-3111 5986
pep-3112 4886
pep-3113 10532
pep-3114 8194
pep-3115 13454
pep-3116 21130
pep-3117 8616
pep-3118 35802
pep-3119 37067
pep-3120 3737
pep-3121 6045
pep-3122 10259
pep-3123 4570
pep-3124 39127
pep-3125 7520
pep-3126 11673
pep-3127 20129
pep-3128 16469
pep-3129 3618
pep-3130 7091
pep-3131 11156
pep-3132 5577
pep-3133 16429
pep-3134 21811
pep-3135 7553
pep-3136 15484
pep-3137 12313
pep-3138 11862
pep-3139 4571
pep-3140 6518
pep-3141 18275
pep-3142 3884
pep-3143 18127
pep-3144 15804
pep-3145 5845
pep-3146 68735
pep-3147 22938
pep-3148 17299
pep-3149 12383
pep-3150 31106
pep-3151 34475
pep-3152 5123
pep-3153 12243
pep-3154 5106
pep-3155 3585
pep-3333 81955
README 494
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/test_docfinder.py", line 47, in <module>
    print get_document('pep-0237')[:100]
TypeError: 'NoneType' object has no attribute '__getitem__'
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/test_docfinder.py", line 47, in <module>
    print get_document('pep-0237')[:100]
TypeError: 'NoneType' object has no attribute '__getitem__'
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
PEP: 237
Title: Unifying Long Integers and Integers
Version: $Revision$
Last-Modified: $Date$
Author
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/test_docfinder.py", line 47, in <module>
    print get_document('pep-0237-missnig')[:100]
  File "/Users/mike/teaching/2017-04-24/docfinder.py", line 115, in get_document
    return bz2.decompress(row[0])
TypeError: 'NoneType' object has no attribute '__getitem__'
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/test_docfinder.py", line 47, in <module>
    print get_document('pep-0237-missnig')[:100]
  File "/Users/mike/teaching/2017-04-24/docfinder.py", line 116, in get_document
    raise UnknownURI(uri)
UnknownURI: pep-0237-missnig
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
pep-0001 21093
pep-0002 8338
pep-0003 2233
pep-0004 10523
pep-0005 3099
pep-0006 8439
pep-0007 6840
pep-0008 32509
pep-0009 9011
pep-0010 1989
pep-0011 6259
pep-0012 22407
pep-0020 1537
pep-0042 11386
pep-0100 42745
pep-0101 25522
pep-0102 20843
pep-0160 2253
pep-0200 14252
pep-0201 9674
pep-0202 2276
pep-0203 14147
pep-0204 11030
pep-0205 20340
pep-0206 3256
pep-0207 18802
pep-0208 10099
pep-0209 29438
pep-0210 298
pep-0211 6783
pep-0212 4902
pep-0213 8536
pep-0214 13522
pep-0215 4804
pep-0216 5438
pep-0217 1720
pep-0218 8029
pep-0219 8520
pep-0220 745
pep-0221 3978
pep-0222 8830
pep-0223 7504
pep-0224 8866
pep-0225 29809
pep-0226 4469
pep-0227 21474
pep-0228 4663
pep-0229 4214
pep-0230 14446
pep-0231 21675
pep-0232 8003
pep-0233 3051
pep-0234 20856
pep-0235 6657
pep-0236 13914
pep-0237 14330
pep-0238 23422
pep-0239 4782
pep-0240 3077
pep-0241 7703
pep-0242 8974
pep-0243 6702
pep-0244 6335
pep-0245 18731
pep-0246 32205
pep-0247 6400
pep-0248 12098
pep-0249 45244
pep-0250 5401
pep-0251 2560
pep-0252 32627
pep-0253 43135
pep-0254 651
pep-0255 20503
pep-0256 10434
pep-0257 11682
pep-0258 35850
pep-0259 3935
pep-0260 2283
pep-0261 10423
pep-0262 12859
pep-0263 8558
pep-0264 4868
pep-0265 7316
pep-0266 19657
pep-0267 10680
pep-0268 8856
pep-0269 7196
pep-0270 2369
pep-0271 1592
pep-0272 9070
pep-0273 8663
pep-0274 5133
pep-0275 12309
pep-0276 16273
pep-0277 4382
pep-0278 9188
pep-0279 8764
pep-0280 19835
pep-0281 4341
pep-0282 22943
pep-0283 11335
pep-0284 10687
pep-0285 17004
pep-0286 3568
pep-0287 32544
pep-0288 5529
pep-0289 10641
pep-0290 13748
pep-0291 6138
pep-0292 8200
pep-0293 15988
pep-0294 3085
pep-0295 3142
pep-0296 16807
pep-0297 3649
pep-0298 8767
pep-0299 3508
pep-0301 14086
pep-0302 28402
pep-0303 7489
pep-0304 13573
pep-0305 14881
pep-0306 3303
pep-0307 34989
pep-0308 17468
pep-0309 10100
pep-0310 8309
pep-0311 9588
pep-0312 5894
pep-0313 4621
pep-0314 9597
pep-0315 4024
pep-0316 15048
pep-0317 14865
pep-0318 30935
pep-0319 15878
pep-0320 6898
pep-0321 4359
pep-0322 5836
pep-0323 19812
pep-0324 18933
pep-0325 10752
pep-0326 20788
pep-0327 40620
pep-0328 10696
pep-0329 9942
pep-0330 9059
pep-0331 8047
pep-0332 2404
pep-0333 75600
pep-0334 13247
pep-0335 17286
pep-0336 2984
pep-0337 5020
pep-0338 13713
pep-0339 22727
pep-0340 22880
pep-0341 3006
pep-0342 26155
pep-0343 37815
pep-0344 21542
pep-0345 16422
pep-0346 44697
pep-0347 10942
pep-0348 19558
pep-0349 5267
pep-0350 25013
pep-0351 5073
pep-0352 11284
pep-0353 9578
pep-0354 8006
pep-0355 20431
pep-0356 5616
pep-0357 8522
pep-0358 10677
pep-0359 18232
pep-0360 3816
pep-0361 8888
pep-0362 12998
pep-0363 8679
pep-0364 10558
pep-0365 4860
pep-0366 5844
pep-0367 19947
pep-0368 34446
pep-0369 8871
pep-0370 8005
pep-0371 17421
pep-0372 12222
pep-0373 1543
pep-0374 54373
pep-0375 1700
pep-0376 23345
pep-0377 9724
pep-0378 9287
pep-0379 5247
pep-0380 17451
pep-0381 11665
pep-0382 8818
pep-0383 8230
pep-0384 13889
pep-0385 19368
pep-0386 18562
pep-0387 4226
pep-0389 12816
pep-0390 7822
pep-0391 27221
pep-0392 1879
pep-0393 18819
pep-0394 9999
pep-0395 11398
pep-0396 10635
pep-0397 18326
pep-0398 2432
pep-0399 8384
pep-0400 11410
pep-0401 4293
pep-0402 28759
pep-0403 10589
pep-0404 27552
pep-0444 70029
pep-0628 3599
pep-0666 4324
pep-0754 6401
pep-3000 6080
pep-3001 4576
pep-3002 4692
pep-3003 5988
pep-3099 7751
pep-3100 17744
pep-3101 34990
pep-3102 6903
pep-3103 25030
pep-3104 21700
pep-3105 4855
pep-3106 11245
pep-3107 11028
pep-3108 30384
pep-3109 7740
pep-3110 8554
pep-3111 5986
pep-3112 4886
pep-3113 10532
pep-3114 8194
pep-3115 13454
pep-3116 21130
pep-3117 8616
pep-3118 35802
pep-3119 37067
pep-3120 3737
pep-3121 6045
pep-3122 10259
pep-3123 4570
pep-3124 39127
pep-3125 7520
pep-3126 11673
pep-3127 20129
pep-3128 16469
pep-3129 3618
pep-3130 7091
pep-3131 11156
pep-3132 5577
pep-3133 16429
pep-3134 21811
pep-3135 7553
pep-3136 15484
pep-3137 12313
pep-3138 11862
pep-3139 4571
pep-3140 6518
pep-3141 18275
pep-3142 3884
pep-3143 18127
pep-3144 15804
pep-3145 5845
pep-3146 68735
pep-3147 22938
pep-3148 17299
pep-3149 12383
pep-3150 31106
pep-3151 34475
pep-3152 5123
pep-3153 12243
pep-3154 5106
pep-3155 3585
pep-3333 81955
README 494
PEP: 237
Title: Unifying Long Integers and Integers
Version: $Revision$
Last-Modified: $Date$
Author
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
PEP: 237
Title: Unifying Long Integers and Integers
Version: $Revision$
Last-Modified: $Date$
Author
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
PEP: 383
Title: Non-decodable Bytes in System Character Interfaces
Version: $Revision$
Last-Modified
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
PEP: 237
Title: Unifying Long Integers and Integers
Version: $Revision$
Last-Modified: $Date$
Author
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/test_docfinder.py", line 51, in <module>
    pprint.pprint(search('zip')[:10])
TypeError: 'NoneType' object has no attribute '__getitem__'
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/test_docfinder.py", line 51, in <module>
    pprint.pprint(search('zip')[:10])
TypeError: 'NoneType' object has no attribute '__getitem__'
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
[u'pep-0201',
 u'pep-0202',
 u'pep-0212',
 u'pep-0243',
 u'pep-0273',
 u'pep-0277',
 u'pep-0279',
 u'pep-0302',
 u'pep-0361',
 u'pep-0382']
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
[u'pep-0273',
 u'pep-0201',
 u'pep-0212',
 u'pep-0202',
 u'pep-3099',
 u'pep-0243',
 u'pep-0382',
 u'pep-0279',
 u'pep-0302',
 u'pep-0277']
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
[u'pep-0273',
 u'pep-0201',
 u'pep-0212',
 u'pep-0202',
 u'pep-3099',
 u'pep-0243',
 u'pep-0382',
 u'pep-0279',
 u'pep-0302',
 u'pep-0277']
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
[u'pep-0273',
 u'pep-0201',
 u'pep-0212',
 u'pep-0202',
 u'pep-3099',
 u'pep-0243',
 u'pep-0382',
 u'pep-0279',
 u'pep-0302',
 u'pep-0277']
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
[u'pep-0273',
 u'pep-0201',
 u'pep-0212',
 u'pep-0202',
 u'pep-3099',
 u'pep-0243',
 u'pep-0382',
 u'pep-0279',
 u'pep-0302',
 u'pep-0277']
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/docfinder.py ===========
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/docfinder.py ===========
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/test_docfinder.py", line 51, in <module>
    pprint.pprint(search('zip', 'barry')[:10])
  File "/Users/mike/teaching/2017-04-24/docfinder.py", line 134, in search
    c.execute(query, (term,))
NameError: global name 'term' is not defined
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
[u'pep-0273',
 u'pep-0201',
 u'pep-0274',
 u'pep-0401',
 u'pep-0251',
 u'pep-0202',
 u'pep-0010',
 u'pep-0212',
 u'pep-0202',
 u'pep-0291']
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
[u'pep-0273',
 u'pep-0201',
 u'pep-0274',
 u'pep-0401',
 u'pep-0251',
 u'pep-0010',
 u'pep-0212',
 u'pep-0202',
 u'pep-0291',
 u'pep-0351']
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
[u'pep-0201',
 u'pep-0273',
 u'pep-0274',
 u'pep-0202',
 u'pep-0401',
 u'pep-0251',
 u'pep-0010',
 u'pep-0212',
 u'pep-0291',
 u'pep-0351']
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
[u'pep-0201',
 u'pep-0273',
 u'pep-0274',
 u'pep-0202',
 u'pep-0401',
 u'pep-0251',
 u'pep-0010',
 u'pep-0212',
 u'pep-0291',
 u'pep-0351']
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
[u'pep-0201',
 u'pep-0273',
 u'pep-0274',
 u'pep-0202',
 u'pep-0401',
 u'pep-0251',
 u'pep-0010',
 u'pep-0212',
 u'pep-0291',
 u'pep-0351']
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/test_docfinder.py =========
['hettinger', 'enumerate']
a 0.043229497775
division 0.0305149396058
to 0.0298792116974
i 0.0228862047044
for 0.020979020979
in 0.018118245391
that 0.0152574698029
python 0.013986013986
be 0.0133502860776
true 0.0123966942149
pep-0001 21093
pep-0002 8338
pep-0003 2233
pep-0004 10523
pep-0005 3099
pep-0006 8439
pep-0007 6840
pep-0008 32509
pep-0009 9011
pep-0010 1989
pep-0011 6259
pep-0012 22407
pep-0020 1537
pep-0042 11386
pep-0100 42745
pep-0101 25522
pep-0102 20843
pep-0160 2253
pep-0200 14252
pep-0201 9674
pep-0202 2276
pep-0203 14147
pep-0204 11030
pep-0205 20340
pep-0206 3256
pep-0207 18802
pep-0208 10099
pep-0209 29438
pep-0210 298
pep-0211 6783
pep-0212 4902
pep-0213 8536
pep-0214 13522
pep-0215 4804
pep-0216 5438
pep-0217 1720
pep-0218 8029
pep-0219 8520
pep-0220 745
pep-0221 3978
pep-0222 8830
pep-0223 7504
pep-0224 8866
pep-0225 29809
pep-0226 4469
pep-0227 21474
pep-0228 4663
pep-0229 4214
pep-0230 14446
pep-0231 21675
pep-0232 8003
pep-0233 3051
pep-0234 20856
pep-0235 6657
pep-0236 13914
pep-0237 14330
pep-0238 23422
pep-0239 4782
pep-0240 3077
pep-0241 7703
pep-0242 8974
pep-0243 6702
pep-0244 6335
pep-0245 18731
pep-0246 32205
pep-0247 6400
pep-0248 12098
pep-0249 45244
pep-0250 5401
pep-0251 2560
pep-0252 32627
pep-0253 43135
pep-0254 651
pep-0255 20503
pep-0256 10434
pep-0257 11682
pep-0258 35850
pep-0259 3935
pep-0260 2283
pep-0261 10423
pep-0262 12859
pep-0263 8558
pep-0264 4868
pep-0265 7316
pep-0266 19657
pep-0267 10680
pep-0268 8856
pep-0269 7196
pep-0270 2369
pep-0271 1592
pep-0272 9070
pep-0273 8663
pep-0274 5133
pep-0275 12309
pep-0276 16273
pep-0277 4382
pep-0278 9188
pep-0279 8764
pep-0280 19835
pep-0281 4341
pep-0282 22943
pep-0283 11335
pep-0284 10687
pep-0285 17004
pep-0286 3568
pep-0287 32544
pep-0288 5529
pep-0289 10641
pep-0290 13748
pep-0291 6138
pep-0292 8200
pep-0293 15988
pep-0294 3085
pep-0295 3142
pep-0296 16807
pep-0297 3649
pep-0298 8767
pep-0299 3508
pep-0301 14086
pep-0302 28402
pep-0303 7489
pep-0304 13573
pep-0305 14881
pep-0306 3303
pep-0307 34989
pep-0308 17468
pep-0309 10100
pep-0310 8309
pep-0311 9588
pep-0312 5894
pep-0313 4621
pep-0314 9597
pep-0315 4024
pep-0316 15048
pep-0317 14865
pep-0318 30935
pep-0319 15878
pep-0320 6898
pep-0321 4359
pep-0322 5836
pep-0323 19812
pep-0324 18933
pep-0325 10752
pep-0326 20788
pep-0327 40620
pep-0328 10696
pep-0329 9942
pep-0330 9059
pep-0331 8047
pep-0332 2404
pep-0333 75600
pep-0334 13247
pep-0335 17286
pep-0336 2984
pep-0337 5020
pep-0338 13713
pep-0339 22727
pep-0340 22880
pep-0341 3006
pep-0342 26155
pep-0343 37815
pep-0344 21542
pep-0345 16422
pep-0346 44697
pep-0347 10942
pep-0348 19558
pep-0349 5267
pep-0350 25013
pep-0351 5073
pep-0352 11284
pep-0353 9578
pep-0354 8006
pep-0355 20431
pep-0356 5616
pep-0357 8522
pep-0358 10677
pep-0359 18232
pep-0360 3816
pep-0361 8888
pep-0362 12998
pep-0363 8679
pep-0364 10558
pep-0365 4860
pep-0366 5844
pep-0367 19947
pep-0368 34446
pep-0369 8871
pep-0370 8005
pep-0371 17421
pep-0372 12222
pep-0373 1543
pep-0374 54373
pep-0375 1700
pep-0376 23345
pep-0377 9724
pep-0378 9287
pep-0379 5247
pep-0380 17451
pep-0381 11665
pep-0382 8818
pep-0383 8230
pep-0384 13889
pep-0385 19368
pep-0386 18562
pep-0387 4226
pep-0389 12816
pep-0390 7822
pep-0391 27221
pep-0392 1879
pep-0393 18819
pep-0394 9999
pep-0395 11398
pep-0396 10635
pep-0397 18326
pep-0398 2432
pep-0399 8384
pep-0400 11410
pep-0401 4293
pep-0402 28759
pep-0403 10589
pep-0404 27552
pep-0444 70029
pep-0628 3599
pep-0666 4324
pep-0754 6401
pep-3000 6080
pep-3001 4576
pep-3002 4692
pep-3003 5988
pep-3099 7751
pep-3100 17744
pep-3101 34990
pep-3102 6903
pep-3103 25030
pep-3104 21700
pep-3105 4855
pep-3106 11245
pep-3107 11028
pep-3108 30384
pep-3109 7740
pep-3110 8554
pep-3111 5986
pep-3112 4886
pep-3113 10532
pep-3114 8194
pep-3115 13454
pep-3116 21130
pep-3117 8616
pep-3118 35802
pep-3119 37067
pep-3120 3737
pep-3121 6045
pep-3122 10259
pep-3123 4570
pep-3124 39127
pep-3125 7520
pep-3126 11673
pep-3127 20129
pep-3128 16469
pep-3129 3618
pep-3130 7091
pep-3131 11156
pep-3132 5577
pep-3133 16429
pep-3134 21811
pep-3135 7553
pep-3136 15484
pep-3137 12313
pep-3138 11862
pep-3139 4571
pep-3140 6518
pep-3141 18275
pep-3142 3884
pep-3143 18127
pep-3144 15804
pep-3145 5845
pep-3146 68735
pep-3147 22938
pep-3148 17299
pep-3149 12383
pep-3150 31106
pep-3151 34475
pep-3152 5123
pep-3153 12243
pep-3154 5106
pep-3155 3585
pep-3333 81955
README 494
PEP: 237
Title: Unifying Long Integers and Integers
Version: $Revision$
Last-Modified: $Date$
Author
[u'pep-0201',
 u'pep-0273',
 u'pep-0274',
 u'pep-0202',
 u'pep-0401',
 u'pep-0251',
 u'pep-0010',
 u'pep-0212',
 u'pep-0291',
 u'pep-0351']
>>> 
