Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 12:39:47) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> # Python for Engineers, Part 2
>>> # Copyright (c) 2017 Raymond Hettinger
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
>>> 
>>> c = Circle(10)
>>> c.area()
314.159
>>> c.circumference()
62.800000000000004
>>> c
<circuitous.Circle instance at 0x101fa86c8>
>>> 
>>> 
>>> import socket
>>> socket.AF_INET
2
>>> socket.AF_INET = 3
>>> 
=============================== RESTART: Shell ===============================
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/circuitous.py ===========
>>> 
>>> math.pi
3.141592653589793
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/circuitous.py ===========
>>> 
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
>>> 
>>> c = Circle(10)
>>> c.area()
314.1592653589793
>>> c.circumference()
62.83185307179586
>>> 
>>> c
<circuitous.Circle instance at 0x101ea96c8>
>>> 
>>> d = Circle(15)
>>> d
<circuitous.Circle instance at 0x101eaa830>
>>> c
<circuitous.Circle instance at 0x101ea96c8>
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/circuitous.py ===========
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/circuitous.py ===========
>>> 
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
>>> 
>>> c = Circle(10)
>>> c
Circle(radius=10)
>>> 
>>> c = Circle('a')
>>> c
Circle(radius=a)
>>> Circle(radius=a)

Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    Circle(radius=a)
NameError: name 'a' is not defined
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/circuitous.py ===========
>>> c = Circle('a')
>>> c
Circle(radius='a')
>>> Circle(radius='a')
Circle(radius='a')
>>> 
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/circuitous.py ===========
>>> 
>>> print str(5)
5
>>> print repr(5)
5
>>> print str('a')
a
>>> print repr('a')
'a'
>>> print str('a\tb')
a	b
>>> print repr('a\tb')
'a\tb'
>>> 
>>> Circle(radius=a)

Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    Circle(radius=a)
NameError: name 'a' is not defined
>>> Circle(radius='a')
Circle(radius='a')
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/circuitous.py ===========
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/circuitous.py ===========
>>> '11.2' < '2.11'
True
>>> 
>>> 5 + 2j < 2 + 5j

Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    5 + 2j < 2 + 5j
TypeError: no ordering relation is defined for complex numbers
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) (0, 1, 3)
>>> 
>>> Circle.version[1]
1
>>> 
>>> Circle.version[2]
3
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/circuitous.py ===========
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=1, patch=3)
>>> 
>>> Circle.version.major
0
>>> import sys
>>> sys.version_info
sys.version_info(major=2, minor=7, micro=13, releaselevel='final', serial=0)
>>> sys.version_info < (3, 0)
True
>>> Circle.version[:2]
(0, 1)
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=1, patch=3)
The average area of 5 random circles
is
>>> random()
0.4575260495248472
>>> random()
0.22230021438242675
>>> random()
0.6559086459284488
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=1, patch=3)
The average area of 5 random circles
is
>>> circles
[Circle(radius=0.4683503924100506), Circle(radius=0.7188027301951472), Circle(radius=0.8636747590596217), Circle(radius=0.5090329616493608), Circle(radius=0.3592857230466636)]
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=1, patch=3)
The average area of 5 random circles
is
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=1, patch=3)
The average area of 5 random circles
is 1.38013037377
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=1, patch=3)
The average area of 5 random circles
is 1.4304586162
>>> circles
[Circle(radius=0.8210457999311388), Circle(radius=0.327616329539809), Circle(radius=0.7007903055438273), Circle(radius=0.7611232939596159), Circle(radius=0.6517524151502027)]
>>> areas
[2.1177985191302917, 0.33719486588350406, 1.5428583077707105, 1.8199518574595752, 1.3344895307739684]
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=1, patch=3)
The average area of 10000 random circles
is 1.05065183867
>>> circles
<generator object <genexpr> at 0x102643140>
>>> areas
<generator object <genexpr> at 0x103852e10>
>>> 
>>> sorted('fsdfad')
['a', 'd', 'd', 'f', 'f', 's']
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=1, patch=3)
The average area of 10000 random circles
is 1.04044221229
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=1, patch=3)
The average area of 5 random circles
is 1.48767395293
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=1, patch=3)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=1, patch=3)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=1, patch=3)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223
A circle with radius 0.7
has an area 1.53938040026
and a perimeter 4.39822971503
A circle with radius 0.3
has an area 0.282743338823
and a perimeter 1.88495559215
A circle with radius 0.5
has an area 0.785398163397
and a perimeter 3.14159265359
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=1, patch=3)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has an area 1.53938040026
and a perimeter 4.39822971503

A circle with radius 0.3
has an area 0.282743338823
and a perimeter 1.88495559215

A circle with radius 0.5
has an area 0.785398163397
and a perimeter 3.14159265359

>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=1, patch=3)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has an area 1.54
and a perimeter 4.40

A circle with radius 0.3
has an area 0.28
and a perimeter 1.88

A circle with radius 0.5
has an area 0.79
and a perimeter 3.14

>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=1, patch=3)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has an area 1.54
and a perimeter 4.40

A circle with radius 0.3
has an area 0.28
and a perimeter 1.88

A circle with radius 0.5
has an area 0.79
and a perimeter 3.14

>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=1, patch=3)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28
and a perimeter 1.88
and a warm area 0.34

A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95

>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=1, patch=3)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28
and a perimeter 1.88
and a warm area 0.34

A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95

>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=1, patch=3)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28
and a perimeter 1.88
and a warm area 0.34

A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95


Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/circuitous_client.py", line 42, in <module>
    t = Tyre(22)
TypeError: this constructor takes no arguments
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=1, patch=3)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28
and a perimeter 1.88
and a warm area 0.34

A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95

a tire of radius 22
has an area 1520.53

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/circuitous_client.py", line 45, in <module>
    print 'and a circumference %.2f' % t.circumference()
  File "/Users/mike/teaching/2017-04-24/circuitous_client.py", line 40, in circumference
    return 1.25 * self.circumference()
  File "/Users/mike/teaching/2017-04-24/circuitous_client.py", line 40, in circumference
    return 1.25 * self.circumference()
  File "/Users/mike/teaching/2017-04-24/circuitous_client.py", line 40, in circumference
    return 1.25 * self.circumference()
  File "/Users/mike/teaching/2017-04-24/circuitous_client.py", line 40, in circumference
    return 1.25 * self.circumference()
  File "/Users/mike/teaching/2017-04-24/circuitous_client.py", line 40, in circumference
    return 1.25 * self.circumference()
  File "/Users/mike/teaching/2017-04-24/circuitous_client.py", line 40, in circumference
    return 1.25 * self.circumference()
  File "/Users/mike/teaching/2017-04-24/circuitous_client.py", line 40, in circumference
    return 1.25 * self.circumference()
  File "/Users/mike/teaching/2017-04-24/circuitous_client.py", line 40, in circumference
    return 1.25 * self.circumference()
  File "/Users/mike/teaching/2017-04-24/circuitous_client.py", line 40, in circumference
    return 1.25 * self.circumference()
  File "/Users/mike/teaching/2017-04-24/circuitous_client.py", line 40, in circumference
    return 1.25 * self.circumference()
  File "/Users/mike/teaching/2017-04-24/circuitous_client.py", line 40, in circumference
    return 1.25 * self.circumference()
  File "/Users/mike/teaching/2017-04-24/circuitous_client.py", line 40, in circumference
    return 1.25 * self.circumference()
  File "/Users/mike/teaching/2017-04-24/circuitous_client.py", line 40, in circumference
    return 1.25 * self.circumference()
  File "/Users/mike/teaching/2017-04-24/circuitous_client.py", line 40, in circumference
    return 1.25 * self.circumference()
  File "/Users/mike/teaching/2017-04-24/circuitous_client.py", line 40, in circumference
    return 1.25 * self.circumference()
  File "/Users/mike/teaching/2017-04-24/circuitous_client.py", line 40, in circumference
    return 1.25 * self.circumference()
  File "/Users/mike/teaching/2017-04-24/circuitous_client.py", line 40, in circumference
    return 1.25 * self.circumference()

=============================== RESTART: Shell ===============================
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=1, patch=3)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28
and a perimeter 1.88
and a warm area 0.34

A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95

a tire of radius 22
has an area 1520.53

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/circuitous_client.py", line 45, in <module>
    print 'and a circumference %.2f' % t.circumference()
  File "/Users/mike/teaching/2017-04-24/circuitous_client.py", line 40, in circumference
    return 1.25 * Circle.circumference()
TypeError: unbound method circumference() must be called with Circle instance as first argument (got nothing instead)
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=1, patch=3)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28
and a perimeter 1.88
and a warm area 0.34

A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95

a tire of radius 22
has an area 1520.53
and a circumference 172.79
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=1, patch=3)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28
and a perimeter 1.88
and a warm area 0.34

A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95

a tire of radius 22
has an area 1520.53
and a circumference 172.79
>>> t
Circle(radius=22)
>>> 
>>> 
>>> t.__class__
<class __main__.Tyre at 0x10304a530>
>>> 
>>> # dunder     __name__
>>> 
>>> t.__class__.__name__
'Tyre'
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=1, patch=3)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28
and a perimeter 1.88
and a warm area 0.34

A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95

a tire of radius 22
has an area 1520.53
and a circumference 172.79
>>> 
>>> 
>>> t
Tyre(radius=22)
>>> {1, 2, 3}
set([1, 2, 3])
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/circuitous.py ===========
>>> 
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/circuitous.py ===========
>>> 
>>> Circle.
SyntaxError: invalid syntax
>>> Circle.angle_to_grade(7)

Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    Circle.angle_to_grade(7)
TypeError: unbound method angle_to_grade() must be called with Circle instance as first argument (got int instance instead)
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/circuitous.py ===========
>>> Circle.angle_to_grade(7)

Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    Circle.angle_to_grade(7)
TypeError: unbound method angle_to_grade() must be called with Circle instance as first argument (got int instance instead)
>>> Circle(None).angle_to_grade(7)
12.27845609029046
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/circuitous.py ===========
>>> 
>>> 
>>> Circle.angle_to_grade(7)
12.27845609029046
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=2, patch=4)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28
and a perimeter 1.88
and a warm area 0.34

A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95

a tire of radius 22
has an area 1520.53
and a circumference 172.79
a hill of with 7 degree incline
is a 12.28% grade
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=2, patch=4)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28
and a perimeter 1.88
and a warm area 0.34

A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95

a tire of radius 22
has an area 1520.53
and a circumference 172.79
a hill of with 7 degree incline
is a 12% grade
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=2, patch=4)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28
and a perimeter 1.88
and a warm area 0.34

A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95

a tire of radius 22
has an area 1520.53
and a circumference 172.79
a hill of with 7 degree incline is a
12% grade
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=2, patch=4)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28
and a perimeter 1.88
and a warm area 0.34

A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95

a tire of radius 22
has an area 1520.53
and a circumference 172.79
a hill of with 7 degree incline is a
12% grade
>>> 
>>> 
>>> dict()
{}
>>> dict({})
{}
>>> dict([('a', 1)])
{'a': 1}
>>> dict(a=1)
{'a': 1}
>>> 
>>> 
>>> 
>>> # Neilsen's law of websites
>>> # your customer
>>> # spends all their time
>>> # on someone else's website
>>> 
>>> dict({})
{}
>>> dict.fromkeys('abc', 0)
{'a': 0, 'c': 0, 'b': 0}
>>> 
>>> from datetime import datetime
>>> datetime(2017, 4, 25)
datetime.datetime(2017, 4, 25, 0, 0)
>>> datetime(2017, 4, 25, 13)
datetime.datetime(2017, 4, 25, 13, 0)
>>> datetime.fromtimestamp(0)
datetime.datetime(1970, 1, 1, 1, 0)
>>> 
>>> # Class.from_something
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/circuitous.py ===========
>>> 
>>> 
>>> Circle.from_bbd(10)

Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    Circle.from_bbd(10)
TypeError: unbound method from_bbd() must be called with Circle instance as first argument (got int instance instead)
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/circuitous.py ===========
>>> Circle.from_bbd(10)
Circle(radius=7.071067811865475)
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=2, patch=4)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28
and a perimeter 1.88
and a warm area 0.34

A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95

a tire of radius 22
has an area 1520.53
and a circumference 172.79
a hill of with 7 degree incline is a
12% grade

a circle with bounding box diagonal 10
has a radius 7.07
and an area 157.08

>>> 
>>> 
>>> 
>>> t
Tyre(radius=22)
>>> 
>>> dir(Tyre)
['__doc__', '__init__', '__module__', '__repr__', 'angle_to_grade', 'area', 'circumference', 'from_bbd', 'version']
>>> 
>>> Tyre.angle_to_grade(10)
17.632698070846498
>>> help(Tyre.from_bbd)
Help on function from_bbd in module circuitous:

from_bbd(diagonal)
    Construct a new Circle from bounding box diagonal

>>> 
>>> Tyre.from_bbd(20)
Circle(radius=14.14213562373095)
>>> 
>>> t = Tyre.from_bbd(20)
>>> t
Circle(radius=14.14213562373095)
>>> t.__class__
<class circuitous.Circle at 0x10385d4c8>
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=3, patch=0)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28
and a perimeter 1.88
and a warm area 0.34

A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95

a tire of radius 22
has an area 1520.53
and a circumference 172.79
a hill of with 7 degree incline is a
12% grade

a circle with bounding box diagonal 10
has a radius 7.07
and an area 157.08

>>> 
>>> 
>>> Tyre.from_bbd(10)
Circle(radius=7.071067811865475)
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=3, patch=0)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28
and a perimeter 1.88
and a warm area 0.34

A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95

a tire of radius 22
has an area 1520.53
and a circumference 172.79
a hill of with 7 degree incline is a
12% grade

a circle with bounding box diagonal 10
has a radius 7.07
and an area 157.08

>>> Tyre.from_bbd(10)
Tyre(radius=7.071067811865475)
>>> 
>>> 
>>> c = Circle(10)
>>> c.from_bbd(10)
Circle(radius=7.071067811865475)
>>> 
>>> 
>>> 
>>> t = Tyre(10)
>>> t.from_bbd(20)
Tyre(radius=14.14213562373095)
>>> t
Tyre(radius=10)
>>> 
>>> 
>>> u = t.from_bbd(20)
>>> u
Tyre(radius=14.14213562373095)
>>> t
Tyre(radius=10)
>>> 
>>> 
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=3, patch=1)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28
and a perimeter 1.88
and a warm area 0.34

A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95

a tire of radius 22
has an area 1520.53
and a circumference 172.79
a hill of with 7 degree incline is a
12% grade

a circle with bounding box diagonal 10
has a radius 7.07
and an area 157.08

>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=3, patch=1)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28
and a perimeter 1.88
and a warm area 0.34

A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95

a tire of radius 22
has an area 1520.53
and a circumference 172.79
a hill of with 7 degree incline is a
12% grade

a circle with bounding box diagonal 10
has a radius 7.07
and an area 157.08

government inspection
{'diameter': 20.0}
10.0
314.159265359
{'diameter': 40.0}
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=3, patch=1)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28
and a perimeter 1.88
and a warm area 0.34

A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95

a tire of radius 22
has an area 1520.53
and a circumference 172.79
a hill of with 7 degree incline is a
12% grade

a circle with bounding box diagonal 10
has a radius 7.07
and an area 157.08

government inspection
{'radius': 10}
10
314.159265359
{'radius': 20}
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=3, patch=1)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28
and a perimeter 1.88
and a warm area 0.34

A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95

a tire of radius 22
has an area 1520.53
and a circumference 172.79
a hill of with 7 degree incline is a
12% grade

a circle with bounding box diagonal 10
has a radius 7.07
and an area 157.08

government inspection
{'diameter': 20.0}
10.0
314.159265359
{'diameter': 40.0}
>>> 
>>> 
>>> len(c)

Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    len(c)
TypeError: object of type 'Circle' has no len()
>>> c + c

Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    c + c
TypeError: unsupported operand type(s) for +: 'Circle' and 'Circle'
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/circuitous_client.py", line 5, in <module>
    from circuitous import Circle
  File "/Users/mike/teaching/2017-04-24/circuitous.py", line 37, in <module>
    class Circle(object):
  File "/Users/mike/teaching/2017-04-24/circuitous.py", line 46, in Circle
    radius = property(get_radius, set_radius)
NameError: name 'get_radius' is not defined
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/circuitous.py ===========
hello! defining a class!
>>> Circle
<class '__main__.Circle'>
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=3, patch=1)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28

and a perimeter 1.88
and a warm area 0.34


A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95

a tire of radius 22
has an area 1520.53
and a circumference 172.79
a hill of with 7 degree incline is a
12% grade

a circle with bounding box diagonal 10
has a radius 7.07
and an area 157.08

government inspection
{'diameter': 20.0}
10.0
314.159265359
{'diameter': 40.0}
>>> 
>>> 
>>> 
>>> c.foo = 5
>>> 
>>> c.__dict__['foo'] = 5
>>> 
>>> c.foo
5
>>> c.__dict__['foo']
5
>>> 
>>> 
>>> dir(c)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'angle_to_grade', 'area', 'circumference', 'diameter', 'foo', 'from_bbd', 'get_radius', 'radius', 'set_radius', 'version']
>>> 
>>> 
>>> c.get_radius()
20.0
>>> c.radius
20.0
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=3, patch=1)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/circuitous_client.py", line 18, in <module>
    print 'is', sum(areas) / n
  File "/Users/mike/teaching/2017-04-24/circuitous_client.py", line 15, in <genexpr>
    areas = (c.area() for c in circles)
  File "/Users/mike/teaching/2017-04-24/circuitous_client.py", line 14, in <genexpr>
    circles = (Circle(random()) for i in xrange(n))
  File "/Users/mike/teaching/2017-04-24/circuitous.py", line 44, in __init__
    self.radius = radius
AttributeError: can't set attribute
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=3, patch=1)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28
and a perimeter 1.88
and a warm area 0.34

A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95

a tire of radius 22
has an area 1520.53
and a circumference 172.79
a hill of with 7 degree incline is a
12% grade

a circle with bounding box diagonal 10
has a radius 7.07
and an area 157.08

government inspection
{'diameter': 20.0}
10.0
314.159265359
{'diameter': 40.0}
>>> 
>>> 
>>> c.radius
20.0
>>> dir(c)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'angle_to_grade', 'area', 'circumference', 'diameter', 'from_bbd', 'radius', 'version']
>>> 
>>> 
>>> c
Circle(radius=20.0)
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=3, patch=1)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28
and a perimeter 1.88
and a warm area 0.34

A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95

a tire of radius 22
has an area 1520.53
and a circumference 172.79
a hill of with 7 degree incline is a
12% grade

a circle with bounding box diagonal 10
has a radius 7.07
and an area 157.08

government inspection
{'diameter': 20.0}
10.0
314.159265359
{'diameter': 40.0}
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/circuitous.py ===========
>>> 
>>> c = Circle(10)
setting the radius 10
>>> c.radius
getting the radius
10.0
>>> 
>>> c.radius = 20
setting the radius 20
>>> 
>>> c.__dict__
{'diameter': 40.0}
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=3, patch=2)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is setting the radius 0.639426798458
getting the radius
setting the radius 0.0250107552227
getting the radius
setting the radius 0.275029318369
getting the radius
setting the radius 0.223210738149
getting the radius
setting the radius 0.736471214164
getting the radius
0.676916567223

setting the radius 0.7
setting the radius 0.3
setting the radius 0.5
A circle with radius getting the radius
0.7
getting the radius
has a cold area 1.54
getting the radius
and a perimeter 4.40
getting the radius
setting the radius 0.77
getting the radius
and a warm area 1.86

A circle with radius getting the radius
0.3
getting the radius
has a cold area 0.28
getting the radius
and a perimeter 1.88
getting the radius
setting the radius 0.33
getting the radius
and a warm area 0.34

A circle with radius getting the radius
0.5
getting the radius
has a cold area 0.79
getting the radius
and a perimeter 3.14
getting the radius
setting the radius 0.55
getting the radius
and a warm area 0.95

setting the radius 22
a tire of radius 22
getting the radius
has an area 2375.83
getting the radius
and a circumference 172.79
a hill of with 7 degree incline is a
12% grade

setting the radius 7.07106781187
a circle with bounding box diagonal 10
getting the radius
has a radius 7.07
getting the radius
and an area 157.08

government inspection
setting the radius 10
{'diameter': 20.0}
getting the radius
10.0
getting the radius
314.159265359
setting the radius 20
{'diameter': 40.0}
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=3, patch=2)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28
and a perimeter 1.88
and a warm area 0.34

A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95

a tire of radius 22
has an area 2375.83
and a circumference 172.79
a hill of with 7 degree incline is a
12% grade

a circle with bounding box diagonal 10
has a radius 7.07
and an area 157.08

government inspection
{'diameter': 20.0}
10.0
314.159265359
{'diameter': 40.0}
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=3, patch=2)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28
and a perimeter 1.88
and a warm area 0.34

A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95

a tire of radius 22
has an area 1520.53
and a circumference 172.79
a hill of with 7 degree incline is a
12% grade

a circle with bounding box diagonal 10
has a radius 7.07
and an area 157.08

government inspection
{'diameter': 20.0}
10.0
314.159265359
{'diameter': 40.0}
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=3, patch=2)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28
and a perimeter 1.88
and a warm area 0.34

A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95

a tire of radius 22
has an area 1520.53
and a circumference 172.79
a hill of with 7 degree incline is a
12% grade

a circle with bounding box diagonal 10
has a radius 7.07
and an area 157.08

government inspection
{'diameter': 20.0}
10.0
314.159265359
{'diameter': 40.0}
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=3, patch=2)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28
and a perimeter 1.88
and a warm area 0.34

A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95

a tire of radius 22
has an area 2375.83
and a circumference 172.79
a hill of with 7 degree incline is a
12% grade

a circle with bounding box diagonal 10
has a radius 7.07
and an area 157.08

government inspection
{'diameter': 20.0}
10.0
314.159265359
{'diameter': 40.0}
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=3, patch=2)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28
and a perimeter 1.88
and a warm area 0.34

A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95

a tire of radius 22
has an area 1520.53
and a circumference 172.79
a hill of with 7 degree incline is a
12% grade

a circle with bounding box diagonal 10
has a radius 7.07
and an area 157.08

government inspection
{'diameter': 20.0}
10.0
314.159265359
{'diameter': 40.0}
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=3, patch=2)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28
and a perimeter 1.88
and a warm area 0.34

A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95

a tire of radius 22
has an area 1520.53
and a circumference 172.79
a hill of with 7 degree incline is a
12% grade

a circle with bounding box diagonal 10
has a radius 7.07
and an area 157.08

government inspection
{'diameter': 20.0}
10.0
314.159265359
{'diameter': 40.0}
>>> 
>>> 
>>> dir(Circle)
['_Circle__circumference', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'angle_to_grade', 'area', 'circumference', 'from_bbd', 'radius', 'version']
>>> 
>>> dir(Tyre)
['_Circle__circumference', '_Tyre__circumference', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'angle_to_grade', 'area', 'circumference', 'from_bbd', 'radius', 'version']
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=3, patch=2)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28
and a perimeter 1.88
and a warm area 0.34

A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95

a tire of radius 22
has an area 2375.83
and a circumference 172.79
a hill of with 7 degree incline is a
12% grade

a circle with bounding box diagonal 10
has a radius 7.07
and an area 157.08

government inspection
{'diameter': 20.0}
10.0
314.159265359
{'diameter': 40.0}
>>> 
======= RESTART: /Users/mike/teaching/2017-04-24/circuitous_client.py =======
A proposal to research the areas of circles
with Circuitous(tm) Version(major=0, minor=3, patch=2)
The average area of 5 random circles
seeded with the Answer to Life and Everything
is 0.676916567223

A circle with radius 0.7
has a cold area 1.54
and a perimeter 4.40
and a warm area 1.86

A circle with radius 0.3
has a cold area 0.28
and a perimeter 1.88
and a warm area 0.34

A circle with radius 0.5
has a cold area 0.79
and a perimeter 3.14
and a warm area 0.95

a tire of radius 22
has an area 1520.53
and a circumference 172.79
a hill of with 7 degree incline is a
12% grade

a circle with bounding box diagonal 10
has a radius 7.07
and an area 157.08

government inspection
{'diameter': 20.0}
10.0
314.159265359
{'diameter': 40.0}
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/circuitous.py ===========
{'__module__': '__main__', 'area': <function area at 0x103864c08>, 'circumference': <function circumference at 0x103864c80>, 'angle_to_grade': <staticmethod object at 0x103848c58>, 'from_bbd': <classmethod object at 0x103848c20>, 'version': Version(major=0, minor=3, patch=2), 'radius': <property object at 0x10385fe68>, '__repr__': <function __repr__ at 0x103864b90>, '_Circle__circumference': <function circumference at 0x103864c80>, '__doc__': 'an advanced circle analytics toolkit', '__init__': <function __init__ at 0x1038649b0>}
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/circuitous.py ===========
{'__module__': '__main__', 'area': <function area at 0x102864c08>, 'circumference': <function circumference at 0x102864c80>, 'angle_to_grade': <staticmethod object at 0x102848c58>, 'from_bbd': <classmethod object at 0x102848c20>, 'version': Version(major=0, minor=3, patch=2), 'radius': <property object at 0x10285fe68>, '__repr__': <function __repr__ at 0x102864b90>, '_Circle__circumference': <function circumference at 0x102864c80>, '__doc__': 'an advanced circle analytics toolkit', '__init__': <function __init__ at 0x1028649b0>}
>>> 
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/circuitous.py ===========
>>> locs

Traceback (most recent call last):
  File "<pyshell#198>", line 1, in <module>
    locs
NameError: name 'locs' is not defined
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/circuitous.py ===========
>>> locs
{'__module__': '__main__', 'area': <function area at 0x103051c08>, 'circumference': <function circumference at 0x103051c80>, 'angle_to_grade': <staticmethod object at 0x103035c58>, 'from_bbd': <classmethod object at 0x103035c20>, 'version': Version(major=0, minor=3, patch=2), 'radius': <property object at 0x10304ce68>, '__repr__': <function __repr__ at 0x103051b90>, '_Circle__circumference': <function circumference at 0x103051c80>, '__doc__': 'an advanced circle analytics toolkit', '__init__': <function __init__ at 0x1030519b0>}
>>> locs == Circle.__dict__
False
>>> set(locs) == set(Circle.__dict__)
False
>>> set(locs) & set(Circle.__dict__)
set(['__module__', 'area', 'circumference', 'angle_to_grade', 'from_bbd', 'version', 'radius', '__repr__', '_Circle__circumference', '__doc__', '__init__'])
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/circuitous.py ===========
{'__module__': '__main__', 'area': <function area at 0x103864c08>, 'circumference': <function circumference at 0x103864c80>, 'from_bbd': <classmethod object at 0x103848c20>, 'version': Version(major=0, minor=3, patch=2), 'radius': <property object at 0x10385fe68>, '__repr__': <function __repr__ at 0x103864b90>, '_Circle__circumference': <function circumference at 0x103864c80>, '__doc__': 'an advanced circle analytics toolkit', '__init__': <function __init__ at 0x1038649b0>}
>>> 
>>> set(locs) & set(Circle.__dict__)
set(['__module__', 'area', 'circumference', 'angle_to_grade', 'from_bbd', 'version', 'radius', '__repr__', '_Circle__circumference', '__doc__', '__init__'])
>>> set(locs) - set(Circle.__dict__)
set([])
>>> set(Circle.__dict__) - set(locs)
set(['__dict__', '__weakref__'])
>>> 
>>> 
>>> object
<type 'object'>
>>> 
>>> 
>>> a = []
>>> a.append(a)
>>> a
[[...]]
>>> 
>>> del a
>>> 
>>> 
>>> a = []
>>> a.append(a)
>>> a[0]
[[...]]
>>> 
>>> import sys
>>> sys.getrefcount(a)
4
>>> 
>>> 
>>> del a
>>> 
>>> 
>>> # lunch until 1:40pm
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/missing.py ============
>>> 
>>> 
>>> dir(int)
['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__float__', '__floordiv__', '__format__', '__getattribute__', '__getnewargs__', '__hash__', '__hex__', '__index__', '__init__', '__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', '__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']
>>> 
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/missing.py ============
>>> 
>>> len(Foo())

Traceback (most recent call last):
  File "<pyshell#236>", line 1, in <module>
    len(Foo())
AttributeError: Foo instance has no attribute '__len__'
>>> 
>>> Foo() + Foo()

Traceback (most recent call last):
  File "<pyshell#238>", line 1, in <module>
    Foo() + Foo()
TypeError: unsupported operand type(s) for +: 'instance' and 'instance'
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/missing.py ============
>>> Foo() + Foo()

Traceback (most recent call last):
  File "<pyshell#239>", line 1, in <module>
    Foo() + Foo()
TypeError: unsupported operand type(s) for +: 'Foo' and 'Foo'
>>> len(Foo())

Traceback (most recent call last):
  File "<pyshell#240>", line 1, in <module>
    len(Foo())
TypeError: object of type 'Foo' has no len()
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/missing.py ============
>>> __len__

Traceback (most recent call last):
  File "<pyshell#241>", line 1, in <module>

    __len__
NameError: name '__len__' is not defined
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/missing.py ============
>>> 
>>> 
>>> f = Foo()
>>> f.__class__
<class __main__.Foo at 0x10045f328>
>>> type(f)
<type 'instance'>
>>> 
>>> Foo
<class __main__.Foo at 0x10045f328>
>>> 
>>> 
>>> type(5)
<type 'int'>
>>> 
>>> type(Foo)
<type 'classobj'>
>>> 
>>> 
>>> type(5)
<type 'int'>
>>> type(int)
<type 'type'>
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/missing.py ============
>>> 
>>> type(Foo)
<type 'classobj'>
>>> type(Bar)
<type 'type'>
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> 
>>> dir(dict)
['__class__', '__cmp__', '__contains__', '__delattr__', '__delitem__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues']
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/missing.py ============
>>> 
>>> 
>>> a = AngryDict(a=1, b=2, c=3)
>>> a
{'a': 1, 'c': 3, 'b': 2}
>>> type(a)
<class '__main__.AngryDict'>
>>> a['a']
1
>>> a['z']

Traceback (most recent call last):
  File "<pyshell#275>", line 1, in <module>
    a['z']
  File "/Users/mike/teaching/2017-04-24/missing.py", line 8, in __missing__
    print 'I am so angry %r is missing!' % self.key
AttributeError: 'AngryDict' object has no attribute 'key'
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/missing.py ============
>>> a = AngryDict(a=1, b=2, c=3)
>>> a['z']
I am so angry 'z' is missing!

Traceback (most recent call last):
  File "<pyshell#277>", line 1, in <module>
    a['z']
  File "/Users/mike/teaching/2017-04-24/missing.py", line 9, in __missing__
    raise KeyError(key)
KeyError: 'z'
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/missing.py ============
>>> a['z']

Traceback (most recent call last):
  File "<pyshell#278>", line 1, in <module>
    a['z']
NameError: name 'a' is not defined
>>> a = AngryDict(a=1, b=2, c=3)
>>> a['z']
I am so angry, 'z' is missing!

Traceback (most recent call last):
  File "<pyshell#280>", line 1, in <module>
    a['z']
  File "/Users/mike/teaching/2017-04-24/missing.py", line 9, in __missing__
    raise KeyError(key)
KeyError: 'z'
>>> 
>>> 
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/missing.py ============
>>> z = ZeroDict(a=1, b=2)
>>> z
{'a': 1, 'b': 2}
>>> z['a']
1
>>> z['z']
0
>>> 
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/missing.py ============
>>> 
>>> l = ListDict(a=1, b=2)
>>> l
{'a': 1, 'b': 2}
>>> l['z']
[]
>>> l['z'].append(1)
>>> l
{'a': 1, 'b': 2}
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/missing.py ============
>>> l = ListDict()
>>> l
{}
>>> l['a']
[]
>>> l['a'].append(1)
>>> l
{'a': [1]}
>>> 
>>> l['b'].append(10)
>>> l
{'a': [1], 'b': [10]}
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/missing.py ============
>>> 
>>> 
>>> 'The answer was %s yesterday, but is %s today' % (5, 10)
'The answer was 5 yesterday, but is 10 today'
>>> 
>>> 'The answer was %(old)s yesterday, but is %(new)s today' % (5, 10)

Traceback (most recent call last):
  File "<pyshell#306>", line 1, in <module>
    'The answer was %(old)s yesterday, but is %(new)s today' % (5, 10)
TypeError: format requires a mapping
>>> 
>>> 'The answer was %(old)s yesterday, but is %(new)s today' % {'old': 5, 'new': 10}
'The answer was 5 yesterday, but is 10 today'
>>> 
>>> 'The answer was %(old)s yesterday, but is %(new)s today' % {'old': 5}

Traceback (most recent call last):
  File "<pyshell#310>", line 1, in <module>
    'The answer was %(old)s yesterday, but is %(new)s today' % {'old': 5}
KeyError: 'new'
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/missing.py ============
>>> 'The answer was %(old)s yesterday, but is %(new)s today' % DefaultFormatDict({'old': 5})

Traceback (most recent call last):
  File "<pyshell#311>", line 1, in <module>
    'The answer was %(old)s yesterday, but is %(new)s today' % DefaultFormatDict({'old': 5})
TypeError: this constructor takes no arguments
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/missing.py ============
>>> 'The answer was %(old)s yesterday, but is %(new)s today' % DefaultFormatDict({'old': 5})
'The answer was 5 yesterday, but is UNKNOWN today'
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/missing.py ============
>>> 'The answer was %(old)s yesterday, but is %(new)s today' % DefaultFormatDict({'old': 5})
'The answer was 5 yesterday, but is new today'
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/missing.py ============
>>> 'The answer was %(old)s yesterday, but is %(new)s today' % DefaultFormatDict({'old': 5})
'The answer was 5 yesterday, but is %(new)s today'
>>> 
>>> 'The answer was %s yesterday, but is %s today' % (5, 10)
'The answer was 5 yesterday, but is 10 today'
>>> 'The answer was %s yesterday, but is %s today' % 5, 10

Traceback (most recent call last):
  File "<pyshell#317>", line 1, in <module>
    'The answer was %s yesterday, but is %s today' % 5, 10
TypeError: not enough arguments for format string
>>> 
>>> 'The answer was %s yesterday, but is %s today' % (5, 10)
'The answer was 5 yesterday, but is 10 today'
>>> 5 % 3
2
>>> int.__mod__
<slot wrapper '__mod__' of 'int' objects>
>>> str.__mod__
<slot wrapper '__mod__' of 'str' objects>
>>> 
>>> 
>>> 'one %s blank' % (5, 10)

Traceback (most recent call last):
  File "<pyshell#325>", line 1, in <module>
    'one %s blank' % (5, 10)
TypeError: not all arguments converted during string formatting
>>> 'one %s blank' % [5, 10]
'one [5, 10] blank'
>>> 
>>> 
>>> t = (5, 10)
>>> 'one %s blank' % t

Traceback (most recent call last):
  File "<pyshell#330>", line 1, in <module>
    'one %s blank' % t
TypeError: not all arguments converted during string formatting
>>> 
>>> 
>>> 'one %s blank' % t

Traceback (most recent call last):
  File "<pyshell#333>", line 1, in <module>
    'one %s blank' % t
TypeError: not all arguments converted during string formatting

>>> 'one %s blank' % (t,)
'one (5, 10) blank'
>>> 
>>> 
>>> 
>>> 
>>> str.format
<method 'format' of 'str' objects>
>>> 
>>> 
>>> 'one %s blank' % str(t)
'one (5, 10) blank'
>>> 'one %r blank' % str(t)
"one '(5, 10)' blank"
>>> 
>>> 'one %r blank' % t

Traceback (most recent call last):
  File "<pyshell#345>", line 1, in <module>
    'one %r blank' % t
TypeError: not all arguments converted during string formatting
>>> 'one %r blank' % (t,)
'one (5, 10) blank'
>>> 
>>> 'one %r blank' % str(t)
"one '(5, 10)' blank"
>>> 'one %r blank' % (t,)
'one (5, 10) blank'
>>> 
>>> 
>>> 
>>> # defaultdict(list)
>>> # defaultdict(set)
>>> 
>>> list
<type 'list'>
>>> 
>>> list()
[]
>>> 
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/missing.py ============
>>> 
>>> 
>>> d = DefaultDict(list)
>>> d['a']
[]
>>> d
{'a': []}
>>> d['a'].append(1)
>>> 
>>> 
>>> 
>>> factory = list
>>> factory
<type 'list'>
>>> 
>>> factory()
[]
>>> factory()
[]
>>> factory()
[]
>>> 
>>> def five():
	return 5

>>> factory = five
>>> factory()
5
>>> 
>>> 
>>> d = DefaultDict(1)
>>> d['a']

Traceback (most recent call last):
  File "<pyshell#384>", line 1, in <module>
    d['a']
  File "/Users/mike/teaching/2017-04-24/missing.py", line 32, in __missing__
    value = self.factory()
TypeError: 'int' object is not callable
>>> 
>>> 
>>> from collections import defaultdict
>>> defaultdict(5)

Traceback (most recent call last):
  File "<pyshell#388>", line 1, in <module>
    defaultdict(5)
TypeError: first argument must be callable or None
>>> 
>>> defaultdict(None)
defaultdict(None, {})
>>> help(defaultdict)
Help on class defaultdict in module collections:

class defaultdict(__builtin__.dict)
 |  defaultdict(default_factory[, ...]) --> dict with default factory
 |  
 |  The default factory is called without arguments to produce
 |  a new value when a key is not present, in __getitem__ only.
 |  A defaultdict compares equal to a dict with the same items.
 |  All remaining arguments are treated the same as if they were
 |  passed to the dict constructor, including keyword arguments.
 |  
 |  Method resolution order:
 |      defaultdict
 |      __builtin__.dict
 |      __builtin__.object
 |  
 |  Methods defined here:
 |  
 |  __copy__(...)
 |      D.copy() -> a shallow copy of D.
 |  
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |  
 |  __init__(...)
 |      x.__init__(...) initializes x; see help(type(x)) for signature
 |  
 |  __missing__(...)
 |      __missing__(key) # Called by __getitem__ for missing key; pseudo-code:
 |      if self.default_factory is None: raise KeyError((key,))
 |      self[key] = value = self.default_factory()
 |      return value
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)
 |  
 |  copy(...)
 |      D.copy() -> a shallow copy of D.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  default_factory
 |      Factory for default value called by __missing__().
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from __builtin__.dict:
 |  
 |  __cmp__(...)
 |      x.__cmp__(y) <==> cmp(x,y)
 |  
 |  __contains__(...)
 |      D.__contains__(k) -> True if D has a key k, else False
 |  
 |  __delitem__(...)
 |      x.__delitem__(y) <==> del x[y]
 |  
 |  __eq__(...)
 |      x.__eq__(y) <==> x==y
 |  
 |  __ge__(...)
 |      x.__ge__(y) <==> x>=y
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(...)
 |      x.__gt__(y) <==> x>y
 |  
 |  __iter__(...)
 |      x.__iter__() <==> iter(x)
 |  
 |  __le__(...)
 |      x.__le__(y) <==> x<=y
 |  
 |  __len__(...)
 |      x.__len__() <==> len(x)
 |  
 |  __lt__(...)
 |      x.__lt__(y) <==> x<y
 |  
 |  __ne__(...)
 |      x.__ne__(y) <==> x!=y
 |  
 |  __setitem__(...)
 |      x.__setitem__(i, y) <==> x[i]=y
 |  
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |  
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |  
 |  fromkeys(...)
 |      dict.fromkeys(S[,v]) -> New dict with keys from S and values equal to v.
 |      v defaults to None.
 |  
 |  get(...)
 |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
 |  
 |  has_key(...)
 |      D.has_key(k) -> True if D has a key k, else False
 |  
 |  items(...)
 |      D.items() -> list of D's (key, value) pairs, as 2-tuples
 |  
 |  iteritems(...)
 |      D.iteritems() -> an iterator over the (key, value) items of D
 |  
 |  iterkeys(...)
 |      D.iterkeys() -> an iterator over the keys of D
 |  
 |  itervalues(...)
 |      D.itervalues() -> an iterator over the values of D
 |  
 |  keys(...)
 |      D.keys() -> list of D's keys
 |  
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, d is returned if given, otherwise KeyError is raised
 |  
 |  popitem(...)
 |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
 |      2-tuple; but raise KeyError if D is empty.
 |  
 |  setdefault(...)
 |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
 |  
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
 |      If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
 |      In either case, this is followed by: for k in F: D[k] = F[k]
 |  
 |  values(...)
 |      D.values() -> list of D's values
 |  
 |  viewitems(...)
 |      D.viewitems() -> a set-like object providing a view on D's items
 |  
 |  viewkeys(...)
 |      D.viewkeys() -> a set-like object providing a view on D's keys
 |  
 |  viewvalues(...)
 |      D.viewvalues() -> an object providing a view on D's values
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from __builtin__.dict:
 |  
 |  __hash__ = None
 |  
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T

>>> 
>>> d = defaultdict(None)
>>> d['a']

Traceback (most recent call last):
  File "<pyshell#394>", line 1, in <module>
    d['a']
KeyError: 'a'
>>> 
>>> 
>>> d = defaultdict(None, a=1, b=2)
>>> d
defaultdict(None, {'a': 1, 'b': 2})
>>> 
>>> d = defaultdict(None, [('a', 1)])
>>> d = defaultdict(None, {})
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/missing.py ============
>>> DefaultDict(None, a=1, b=2)
{'a': 1, 'b': 2}
>>> DefaultDict(None, {})
{}
>>> DefaultDict(None, [('z', 26)])
{'z': 26}
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/missing.py ============
>>> DefaultDict(None, [('z', 26)])
{'z': 26}
>>> 
>>> DefaultDict(None, [('z', 26)], a=1)
{'a': 1, 'z': 26}
>>> 
>>> 
>>> 
>>> def foo(a, b, c):
	print a
	print b
	print c

	
>>> x = [1, 2, 3]
>>> foo(x[0], x[1], x[2])
1
2
3
>>> foo(*x)
1
2
3
>>> 
>>> 
>>> def bar(*args)
SyntaxError: invalid syntax
>>> def bar(*args):
	print args

	
>>> bar()
()
>>> bar(1, 2, 3, 4)
(1, 2, 3, 4)
>>> 
>>> 
>>> 
>>> 
>>> bar
<function bar at 0x1038e4938>
>>> bar(*[1, 2, 3])
(1, 2, 3)
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/missing.py ============
>>> DefaultDict(None, [('z', 26)], a=1)
[('z', 26)]
{'a': 1, 'z': 26}
>>> d = DefaultDict(None, [('z', 26)], a=1)
[('z', 26)]
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/missing.py ============
>>> d = DefaultDict(None, [('z', 26)], a=1, b=2, c=3)
[('z', 26)]
a 1
c 3
b 2
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/missing.py ============
>>> 
>>> settings
{'h': 40, 'w': 80, 'fg': 'cyan'}
>>> defaults
{'h': 24, 'bg': 'black', 'w': 40, 'fg': 'green'}
>>> 
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/missing.py ============
>>> 
>>> settings['fg']
'cyan'
>>> settings['bg']

Traceback (most recent call last):
  File "<pyshell#442>", line 1, in <module>
    settings['bg']
KeyError: 'bg'
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/missing.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/missing.py", line 45, in <module>
    settings = ChainDict(defaults, {'fg': 'cyan', 'h': 40, 'w': 80})
TypeError: dict expected at most 1 arguments, got 2
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/missing.py ============
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/missing.py ============
>>> 
>>> settings
{'h': 40, 'w': 80, 'fg': 'cyan'}
>>> 
>>> settings['bg']
'black'
>>> settings['z']

Traceback (most recent call last):
  File "<pyshell#447>", line 1, in <module>
    settings['z']
  File "/Users/mike/teaching/2017-04-24/missing.py", line 49, in __missing__
    return self.fallback[key]
KeyError: 'z'
>>> 
>>> 
>>> 
>>> settings['bg'] = 'purple'
>>> settings
{'h': 40, 'bg': 'purple', 'w': 80, 'fg': 'cyan'}
>>> settings['bg']
'purple'
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/withable.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/withable.py", line 33, in <module>
    with ContextManager():
AttributeError: __exit__
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/withable.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/withable.py", line 29, in <module>
    with ContextManager():
AttributeError: __enter__
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/withable.py ============
entering the context
inside the context

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/withable.py", line 33, in <module>
    print 'inside the context'
TypeError: __exit__() takes exactly 1 argument (4 given)
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/withable.py ============
entering the context
inside the context
leaving the context
(None, None, None)
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/withable.py ============
entering the context
inside the context
leaving the context:  (None, None, None)
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/withable.py ============
entering the context
inside the context
leaving the context: (None, None, None)
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/withable.py ============
entering the context
inside the context
42
last line in the context
leaving the context: (None, None, None)
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/withable.py ============
entering the context
inside the context
42
leaving the context: (<type 'exceptions.RuntimeError'>, RuntimeError('oops',), <traceback object at 0x1037a96c8>)

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/withable.py", line 39, in <module>
    raise RuntimeError('oops')
RuntimeError: oops
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/withable.py ============
entering the context
inside the context
42
leaving the context

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/withable.py", line 40, in <module>
    raise RuntimeError('oops')
RuntimeError: oops
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/withable.py ============
entering the context
inside the context
42
leaving the context

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/withable.py", line 42, in <module>
    raise RuntimeError('oops')
RuntimeError: oops
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/withable.py ============
entering the context
inside the context
42
leaving the context
marking exception as handled
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/withable.py ============
entering the context
inside the context
42
leaving the context
marking exception as handled
>>> 
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/withable.py ============
entering the context
inside the context
42
leaving the context
marking exception as handled
>>> 
>>> 
>>> 
>>> 
>>> import sys
>>> sys.stdout
<idlelib.PyShell.PseudoOutputFile object at 0x1038e1890>
>>> 
>>> sys.stderr
<idlelib.PyShell.PseudoOutputFile object at 0x1038e18d0>
>>> 
>>> raise Foo

Traceback (most recent call last):
  File "<pyshell#464>", line 1, in <module>
    raise Foo
NameError: name 'Foo' is not defined
>>> 
>>> 
>>> print 'blue'
blue
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/withable.py ============
red
blue
entering the context
inside the context
42
leaving the context
marking exception as handled
>>> 
>>> help('topics')

Here is a list of available topics.  Enter any topic name to get more help.

ASSERTION           DEBUGGING           LITERALS            SEQUENCEMETHODS2
ASSIGNMENT          DELETION            LOOPING             SEQUENCES
ATTRIBUTEMETHODS    DICTIONARIES        MAPPINGMETHODS      SHIFTING
ATTRIBUTES          DICTIONARYLITERALS  MAPPINGS            SLICINGS
AUGMENTEDASSIGNMENT DYNAMICFEATURES     METHODS             SPECIALATTRIBUTES
BACKQUOTES          ELLIPSIS            MODULES             SPECIALIDENTIFIERS
BASICMETHODS        EXCEPTIONS          NAMESPACES          SPECIALMETHODS
BINARY              EXECUTION           NONE                STRINGMETHODS
BITWISE             EXPRESSIONS         NUMBERMETHODS       STRINGS
BOOLEAN             FILES               NUMBERS             SUBSCRIPTS
CALLABLEMETHODS     FLOAT               OBJECTS             TRACEBACKS
CALLS               FORMATTING          OPERATORS           TRUTHVALUE
CLASSES             FRAMEOBJECTS        PACKAGES            TUPLELITERALS
CODEOBJECTS         FRAMES              POWER               TUPLES
COERCIONS           FUNCTIONS           PRECEDENCE          TYPEOBJECTS
COMPARISON          IDENTIFIERS         PRINTING            TYPES
COMPLEX             IMPORTING           PRIVATENAMES        UNARY
CONDITIONAL         INTEGER             RETURNING           UNICODE
CONTEXTMANAGERS     LISTLITERALS        SCOPING             
CONVERSIONS         LISTS               SEQUENCEMETHODS1    

>>> help('UNICODE')
String literals
***************

String literals are described by the following lexical definitions:

   stringliteral   ::= [stringprefix](shortstring | longstring)
   stringprefix    ::= "r" | "u" | "ur" | "R" | "U" | "UR" | "Ur" | "uR"
                    | "b" | "B" | "br" | "Br" | "bR" | "BR"
   shortstring     ::= "'" shortstringitem* "'" | '"' shortstringitem* '"'
   longstring      ::= "'''" longstringitem* "'''"
                  | '"""' longstringitem* '"""'
   shortstringitem ::= shortstringchar | escapeseq
   longstringitem  ::= longstringchar | escapeseq
   shortstringchar ::= <any source character except "\" or newline or the quote>
   longstringchar  ::= <any source character except "\">
   escapeseq       ::= "\" <any ASCII character>

One syntactic restriction not indicated by these productions is that
whitespace is not allowed between the "stringprefix" and the rest of
the string literal. The source character set is defined by the
encoding declaration; it is ASCII if no encoding declaration is given
in the source file; see section Encoding declarations.

In plain English: String literals can be enclosed in matching single
quotes ("'") or double quotes (""").  They can also be enclosed in
matching groups of three single or double quotes (these are generally
referred to as *triple-quoted strings*).  The backslash ("\")
character is used to escape characters that otherwise have a special
meaning, such as newline, backslash itself, or the quote character.
String literals may optionally be prefixed with a letter "'r'" or
"'R'"; such strings are called *raw strings* and use different rules
for interpreting backslash escape sequences.  A prefix of "'u'" or
"'U'" makes the string a Unicode string.  Unicode strings use the
Unicode character set as defined by the Unicode Consortium and ISO
10646.  Some additional escape sequences, described below, are
available in Unicode strings. A prefix of "'b'" or "'B'" is ignored in
Python 2; it indicates that the literal should become a bytes literal
in Python 3 (e.g. when code is automatically converted with 2to3).  A
"'u'" or "'b'" prefix may be followed by an "'r'" prefix.

In triple-quoted strings, unescaped newlines and quotes are allowed
(and are retained), except that three unescaped quotes in a row
terminate the string.  (A "quote" is the character used to open the
string, i.e. either "'" or """.)

Unless an "'r'" or "'R'" prefix is present, escape sequences in
strings are interpreted according to rules similar to those used by
Standard C.  The recognized escape sequences are:

+-------------------+-----------------------------------+---------+
| Escape Sequence   | Meaning                           | Notes   |
+===================+===================================+=========+
| "\newline"        | Ignored                           |         |
+-------------------+-----------------------------------+---------+
| "\\"              | Backslash ("\")                   |         |
+-------------------+-----------------------------------+---------+
| "\'"              | Single quote ("'")                |         |
+-------------------+-----------------------------------+---------+
| "\""              | Double quote (""")                |         |
+-------------------+-----------------------------------+---------+
| "\a"              | ASCII Bell (BEL)                  |         |
+-------------------+-----------------------------------+---------+
| "\b"              | ASCII Backspace (BS)              |         |
+-------------------+-----------------------------------+---------+
| "\f"              | ASCII Formfeed (FF)               |         |
+-------------------+-----------------------------------+---------+
| "\n"              | ASCII Linefeed (LF)               |         |
+-------------------+-----------------------------------+---------+
| "\N{name}"        | Character named *name* in the     |         |
|                   | Unicode database (Unicode only)   |         |
+-------------------+-----------------------------------+---------+
| "\r"              | ASCII Carriage Return (CR)        |         |
+-------------------+-----------------------------------+---------+
| "\t"              | ASCII Horizontal Tab (TAB)        |         |
+-------------------+-----------------------------------+---------+
| "\uxxxx"          | Character with 16-bit hex value   | (1)     |
|                   | *xxxx* (Unicode only)             |         |
+-------------------+-----------------------------------+---------+
| "\Uxxxxxxxx"      | Character with 32-bit hex value   | (2)     |
|                   | *xxxxxxxx* (Unicode only)         |         |
+-------------------+-----------------------------------+---------+
| "\v"              | ASCII Vertical Tab (VT)           |         |
+-------------------+-----------------------------------+---------+
| "\ooo"            | Character with octal value *ooo*  | (3,5)   |
+-------------------+-----------------------------------+---------+
| "\xhh"            | Character with hex value *hh*     | (4,5)   |
+-------------------+-----------------------------------+---------+

Notes:

1. Individual code units which form parts of a surrogate pair can
   be encoded using this escape sequence.

2. Any Unicode character can be encoded this way, but characters
   outside the Basic Multilingual Plane (BMP) will be encoded using a
   surrogate pair if Python is compiled to use 16-bit code units (the
   default).

3. As in Standard C, up to three octal digits are accepted.

4. Unlike in Standard C, exactly two hex digits are required.

5. In a string literal, hexadecimal and octal escapes denote the
   byte with the given value; it is not necessary that the byte
   encodes a character in the source character set. In a Unicode
   literal, these escapes denote a Unicode character with the given
   value.

Unlike Standard C, all unrecognized escape sequences are left in the
string unchanged, i.e., *the backslash is left in the string*.  (This
behavior is useful when debugging: if an escape sequence is mistyped,
the resulting output is more easily recognized as broken.)  It is also
important to note that the escape sequences marked as "(Unicode only)"
in the table above fall into the category of unrecognized escapes for
non-Unicode string literals.

When an "'r'" or "'R'" prefix is present, a character following a
backslash is included in the string without change, and *all
backslashes are left in the string*.  For example, the string literal
"r"\n"" consists of two characters: a backslash and a lowercase "'n'".
String quotes can be escaped with a backslash, but the backslash
remains in the string; for example, "r"\""" is a valid string literal
consisting of two characters: a backslash and a double quote; "r"\""
is not a valid string literal (even a raw string cannot end in an odd
number of backslashes).  Specifically, *a raw string cannot end in a
single backslash* (since the backslash would escape the following
quote character).  Note also that a single backslash followed by a
newline is interpreted as those two characters as part of the string,
*not* as a line continuation.

When an "'r'" or "'R'" prefix is used in conjunction with a "'u'" or
"'U'" prefix, then the "\uXXXX" and "\UXXXXXXXX" escape sequences are
processed while  *all other backslashes are left in the string*. For
example, the string literal "ur"\u0062\n"" consists of three Unicode
characters: 'LATIN SMALL LETTER B', 'REVERSE SOLIDUS', and 'LATIN
SMALL LETTER N'. Backslashes can be escaped with a preceding
backslash; however, both remain in the string.  As a result, "\uXXXX"
escape sequences are only recognized when there are an odd number of
backslashes.

Related help topics: encodings, unicode, SEQUENCES, STRINGMETHODS,
FORMATTING, TYPES

>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/withable.py ============
red
blue
entering the context
inside the context
42
leaving the context
marking exception as handled
>>> 
>>> 
>>> 
>>> 
============ RESTART: /Users/mike/teaching/2017-04-24/withable.py ============
red
blue
entering the context
inside the context
42
leaving the context
marking exception as handled
>>> 
>>> 
>>> Foo() + 5
1
>>> Foo() + 'a'
2
>>> 
>>> 
>>> 
============== RESTART: /Users/mike/teaching/2017-04-24/dog.py ==============
>>> 
>>> d
{<__main__.Dog instance at 0x1027a7200>: 'my dog'}
>>> 
============== RESTART: /Users/mike/teaching/2017-04-24/dog.py ==============
>>> d
{<__main__.Dog instance at 0x1027aa200>: 'my dog'}
>>> 
============== RESTART: /Users/mike/teaching/2017-04-24/dog.py ==============
>>> d
{Dog(name='Fido'): 'my dog'}
>>> 
>>> d[a]
'my dog'
>>> 
>>> b
Dog(name='Fido')
>>> 
>>> d[b]

Traceback (most recent call last):
  File "<pyshell#489>", line 1, in <module>
    d[b]
KeyError: Dog(name='Fido')
>>> d[a]
'my dog'
>>> a
Dog(name='Fido')
>>> b
Dog(name='Fido')
>>> 
>>> 
>>> hash(a)
271077013
>>> hash(b)
271077017
>>> id(a)
4337232208
>>> id(b)
4337232272
>>> 
============== RESTART: /Users/mike/teaching/2017-04-24/dog.py ==============
>>> d
{Dog(name='Fido'): 'my dog'}
>>> d[a]
'my dog'
>>> d[b]

Traceback (most recent call last):
  File "<pyshell#501>", line 1, in <module>
    d[b]
KeyError: Dog(name='Fido')
>>> 
>>> hash(a) == hash(b)
True
>>> 
>>> d[b] = 'another dog'
>>> d
{Dog(name='Fido'): 'another dog', Dog(name='Fido'): 'my dog'}
>>> 
>>> hash('Fido')
-4328439044073677036
>>> hash(a)
-4328439044073677036
>>> 
============== RESTART: /Users/mike/teaching/2017-04-24/dog.py ==============
>>> 
>>> d[a]
'my dog'
>>> d[b]
'my dog'
>>> 
============== RESTART: /Users/mike/teaching/2017-04-24/dog.py ==============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/dog.py", line 30, in <module>
    d[a] = 'my dog'
TypeError: an integer is required
>>> 
============== RESTART: /Users/mike/teaching/2017-04-24/dog.py ==============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/dog.py", line 31, in <module>
    d[a] = 'my dog'
TypeError: unhashable type: 'Dog'
>>> 
>>> 
>>> object.__hash__
<slot wrapper '__hash__' of 'object' objects>
>>> 
============== RESTART: /Users/mike/teaching/2017-04-24/dog.py ==============
>>> 
>>> hash(a)
271011477
>>> a.__hash__
<method-wrapper '__hash__' of Dog object at 0x10274e950>
>>> a.__hash__()
271011477
>>> 
============== RESTART: /Users/mike/teaching/2017-04-24/dog.py ==============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/dog.py", line 31, in <module>
    d[a] = 'my dog'
TypeError: unhashable instance
>>> 
============== RESTART: /Users/mike/teaching/2017-04-24/dog.py ==============

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/dog.py", line 31, in <module>
    d[a] = 'my dog'
TypeError: unhashable instance
>>> 
============== RESTART: /Users/mike/teaching/2017-04-24/dog.py ==============
>>> d[3.3] = 'number'
>>> d[1.1 + 2.2]

Traceback (most recent call last):
  File "<pyshell#521>", line 1, in <module>
    d[1.1 + 2.2]
KeyError: 3.3000000000000003
>>> 
============== RESTART: /Users/mike/teaching/2017-04-24/dog.py ==============
>>> d
{instance(name='Fido'): 'my dog'}
>>> 
>>> d[a]
'my dog'
>>> 
>>> d.name = 'Rex'

Traceback (most recent call last):
  File "<pyshell#526>", line 1, in <module>
    d.name = 'Rex'
AttributeError: 'dict' object has no attribute 'name'
>>> a.name = 'Rex'
>>> a
instance(name='Rex')
>>> 
============== RESTART: /Users/mike/teaching/2017-04-24/dog.py ==============
>>> 
>>> 
>>> d
{Dog(name='Fido'): 'my dog'}
>>> 
>>> d[a]
'my dog'
>>> 
>>> a.name = 'Rex'
>>> 
>>> d
{Dog(name='Rex'): 'my dog'}
>>> 
>>> hash(a)
-102831656949585790
>>> 
>>> d[a]

Traceback (most recent call last):
  File "<pyshell#541>", line 1, in <module>
    d[a]
KeyError: Dog(name='Rex')
>>> 
>>> 
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/properties.py ===========
>>> PriceRange(5, 10)
PriceRange(5, 10)
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/properties.py ===========
PriceRange(5, 10)
7.5
>>> p.high = 100
>>> p
PriceRange(5, 100)
>>> p.mid
7.5
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/properties.py ===========
PriceRange(5, 10)
<bound method PriceRange.mid of PriceRange(5, 10)>
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/properties.py ===========
PriceRange(5, 10)
7.5
>>> p.mid + 10

Traceback (most recent call last):
  File "<pyshell#548>", line 1, in <module>
    p.mid + 10
TypeError: unsupported operand type(s) for +: 'instancemethod' and 'int'
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/properties.py ===========
PriceRange(5, 10)
7.5
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/properties.py ===========
PriceRange(5, 10)
7.5
>>> 
>>> 
>>> PriceRange.mid
<property object at 0x10385f890>
>>> PriceRange.mid.fget
<function mid at 0x1004fad70>
>>> 
>>> p.mid
7.5
>>> 
>>> p.mid = 100

Traceback (most recent call last):
  File "<pyshell#556>", line 1, in <module>
    p.mid = 100
AttributeError: can't set attribute
>>> PriceRange.mid.fset is None
True
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/properties.py ===========
PriceRange(5, 10)
7.5
>>> 
>>> 
>>> p.mid = 100
>>> p
PriceRange(97.5, 102.5)
>>> p.mid
100.0
>>> 
>>> help(p.mid)
Help on float object:

class float(object)
 |  float(x) -> floating point number
 |  
 |  Convert a string or number to a floating point number, if possible.
 |  
 |  Methods defined here:
 |  
 |  __abs__(...)
 |      x.__abs__() <==> abs(x)
 |  
 |  __add__(...)
 |      x.__add__(y) <==> x+y
 |  
 |  __coerce__(...)
 |      x.__coerce__(y) <==> coerce(x, y)
 |  
 |  __div__(...)
 |      x.__div__(y) <==> x/y
 |  
 |  __divmod__(...)
 |      x.__divmod__(y) <==> divmod(x, y)
 |  
 |  __eq__(...)
 |      x.__eq__(y) <==> x==y
 |  
 |  __float__(...)
 |      x.__float__() <==> float(x)
 |  
 |  __floordiv__(...)
 |      x.__floordiv__(y) <==> x//y
 |  
 |  __format__(...)
 |      float.__format__(format_spec) -> string
 |      
 |      Formats the float according to format_spec.
 |  
 |  __ge__(...)
 |      x.__ge__(y) <==> x>=y
 |  
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |  
 |  __getformat__(...)
 |      float.__getformat__(typestr) -> string
 |      
 |      You probably don't want to use this function.  It exists mainly to be
 |      used in Python's test suite.
 |      
 |      typestr must be 'double' or 'float'.  This function returns whichever of
 |      'unknown', 'IEEE, big-endian' or 'IEEE, little-endian' best describes the
 |      format of floating point numbers used by the C type named by typestr.
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(...)
 |      x.__gt__(y) <==> x>y
 |  
 |  __hash__(...)
 |      x.__hash__() <==> hash(x)
 |  
 |  __int__(...)
 |      x.__int__() <==> int(x)
 |  
 |  __le__(...)
 |      x.__le__(y) <==> x<=y
 |  
 |  __long__(...)
 |      x.__long__() <==> long(x)
 |  
 |  __lt__(...)
 |      x.__lt__(y) <==> x<y
 |  
 |  __mod__(...)
 |      x.__mod__(y) <==> x%y
 |  
 |  __mul__(...)
 |      x.__mul__(y) <==> x*y
 |  
 |  __ne__(...)
 |      x.__ne__(y) <==> x!=y
 |  
 |  __neg__(...)
 |      x.__neg__() <==> -x
 |  
 |  __nonzero__(...)
 |      x.__nonzero__() <==> x != 0
 |  
 |  __pos__(...)
 |      x.__pos__() <==> +x
 |  
 |  __pow__(...)
 |      x.__pow__(y[, z]) <==> pow(x, y[, z])
 |  
 |  __radd__(...)
 |      x.__radd__(y) <==> y+x
 |  
 |  __rdiv__(...)
 |      x.__rdiv__(y) <==> y/x
 |  
 |  __rdivmod__(...)
 |      x.__rdivmod__(y) <==> divmod(y, x)
 |  
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)
 |  
 |  __rfloordiv__(...)
 |      x.__rfloordiv__(y) <==> y//x
 |  
 |  __rmod__(...)
 |      x.__rmod__(y) <==> y%x
 |  
 |  __rmul__(...)
 |      x.__rmul__(y) <==> y*x
 |  
 |  __rpow__(...)
 |      y.__rpow__(x[, z]) <==> pow(x, y[, z])
 |  
 |  __rsub__(...)
 |      x.__rsub__(y) <==> y-x
 |  
 |  __rtruediv__(...)
 |      x.__rtruediv__(y) <==> y/x
 |  
 |  __setformat__(...)
 |      float.__setformat__(typestr, fmt) -> None
 |      
 |      You probably don't want to use this function.  It exists mainly to be
 |      used in Python's test suite.
 |      
 |      typestr must be 'double' or 'float'.  fmt must be one of 'unknown',
 |      'IEEE, big-endian' or 'IEEE, little-endian', and in addition can only be
 |      one of the latter two if it appears to match the underlying C reality.
 |      
 |      Override the automatic determination of C-level floating point type.
 |      This affects how floats are converted to and from binary strings.
 |  
 |  __str__(...)
 |      x.__str__() <==> str(x)
 |  
 |  __sub__(...)
 |      x.__sub__(y) <==> x-y
 |  
 |  __truediv__(...)
 |      x.__truediv__(y) <==> x/y
 |  
 |  __trunc__(...)
 |      Return the Integral closest to x between 0 and x.
 |  
 |  as_integer_ratio(...)
 |      float.as_integer_ratio() -> (int, int)
 |      
 |      Return a pair of integers, whose ratio is exactly equal to the original
 |      float and with a positive denominator.
 |      Raise OverflowError on infinities and a ValueError on NaNs.
 |      
 |      >>> (10.0).as_integer_ratio()
 |      (10, 1)
 |      >>> (0.0).as_integer_ratio()
 |      (0, 1)
 |      >>> (-.25).as_integer_ratio()
 |      (-1, 4)
 |  
 |  conjugate(...)
 |      Return self, the complex conjugate of any float.
 |  
 |  fromhex(...)
 |      float.fromhex(string) -> float
 |      
 |      Create a floating-point number from a hexadecimal string.
 |      >>> float.fromhex('0x1.ffffp10')
 |      2047.984375
 |      >>> float.fromhex('-0x1p-1074')
 |      -4.9406564584124654e-324
 |  
 |  hex(...)
 |      float.hex() -> string
 |      
 |      Return a hexadecimal representation of a floating-point number.
 |      >>> (-0.1).hex()
 |      '-0x1.999999999999ap-4'
 |      >>> 3.14159.hex()
 |      '0x1.921f9f01b866ep+1'
 |  
 |  is_integer(...)
 |      Return True if the float is an integer.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  imag
 |      the imaginary part of a complex number
 |  
 |  real
 |      the real part of a complex number
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T

>>> help(PriceRange)
Help on class PriceRange in module __main__:

class PriceRange(__builtin__.object)
 |  Methods defined here:
 |  
 |  __init__(self, low, high)
 |  
 |  __repr__(self)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  mid

>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/properties.py ===========
PriceRange(5, 10)
7.5
>>> help(PriceRange)
Help on class PriceRange in module __main__:

class PriceRange(__builtin__.object)
 |  Methods defined here:
 |  
 |  __init__(self, low, high)
 |  
 |  __repr__(self)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  mid
 |      Halfway between the low and the high

>>> PriceRange.mid.fset
<function mid at 0x1004fade8>
>>> help(PriceRange.mid.fset)
Help on function mid in module __main__:

mid(self, mid)
    recenter around a new mid-point, keeping the same
    distance between the high and the low

>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/properties.py ===========
PriceRange(5, 10)
7.5
>>> p.mid = 100

Traceback (most recent call last):
  File "<pyshell#569>", line 1, in <module>
    p.mid = 100
AttributeError: can't set attribute
>>> 
>>> dir(p)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'high', 'low', 'mid', 'recenter_around_mid']
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/properties.py ===========
PriceRange(5, 10)
7.5
>>> p.__dict__
{'high': 10, '_low': 5}
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/properties.py ===========
PriceRange(5, 10)
7.5
>>> 
>>> 
>>> p.low = -10

Traceback (most recent call last):
  File "<pyshell#575>", line 1, in <module>
    p.low = -10
  File "/Users/mike/teaching/2017-04-24/properties.py", line 58, in low
    raise ValueError('Must be positive')
ValueError: Must be positive
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/properties.py ===========
PriceRange(5, 10)
7.5
>>> 
>>> 
>>> 
>>> def foo():
	return math.pi

>>> math

Traceback (most recent call last):
  File "<pyshell#582>", line 1, in <module>
    math
NameError: name 'math' is not defined
>>> 
>>> 
>>> def foo():
	return math.pi

>>> 
>>> 
>>> import math
>>> foo()
3.141592653589793
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/properties.py ===========
PriceRange(5, 10)
7.5
>>> 
>>> 
>>> 
>>> p.low = 3
>>> 
>>> 
>>> p.low = 'a'

Traceback (most recent call last):
  File "<pyshell#597>", line 1, in <module>
    p.low = 'a'
  File "/Users/mike/teaching/2017-04-24/properties.py", line 58, in low
    raise TypeError('Expected int or float, got %r' % type(value).__name__)
TypeError: Expected int or float, got 'str'
>>> 
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/properties.py ===========
PriceRange(5, 10)
7.5
>>> PriceRange(0, 'a')

Traceback (most recent call last):
  File "<pyshell#599>", line 1, in <module>
    PriceRange(0, 'a')
  File "/Users/mike/teaching/2017-04-24/properties.py", line 49, in __init__
    self.high = high
  File "/Users/mike/teaching/2017-04-24/properties.py", line 70, in high
    raise TypeError('Expected int or float, got %r' % type(value).__name__)
TypeError: Expected int or float, got 'str'
>>> PriceRange(0, -5)

Traceback (most recent call last):
  File "<pyshell#600>", line 1, in <module>
    PriceRange(0, -5)
  File "/Users/mike/teaching/2017-04-24/properties.py", line 49, in __init__
    self.high = high
  File "/Users/mike/teaching/2017-04-24/properties.py", line 72, in high
    raise ValueError('Must be positive')
ValueError: Must be positive
>>> 
>>> 
>>> __dict__

Traceback (most recent call last):
  File "<pyshell#603>", line 1, in <module>
    __dict__
NameError: name '__dict__' is not defined
>>> p.__dict__
{'_high': 10, '_low': 5}
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/properties.py ===========

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/properties.py", line 43, in <module>
    import validators
  File "/Users/mike/teaching/2017-04-24/validators.py", line 10
    def is_positive(value)
                         ^
SyntaxError: invalid syntax
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/properties.py ===========

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/properties.py", line 92, in <module>
    p = PriceRange(5, 10)
  File "/Users/mike/teaching/2017-04-24/properties.py", line 51, in __init__
    self.high = high
  File "/Users/mike/teaching/2017-04-24/properties.py", line 71, in high
    self._high = value
AttributeError: 'PriceRange' object has no attribute '_high'
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/properties.py ===========
PriceRange(5, 10)
7.5
>>> _high

Traceback (most recent call last):
  File "<pyshell#605>", line 1, in <module>
    _high
NameError: name '_high' is not defined
>>> 
>>> 
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/properties.py ===========
PriceRange(5, 10)
7.5
>>> 
>>> 
>>> p.__dict__

Traceback (most recent call last):
  File "<pyshell#610>", line 1, in <module>
    p.__dict__
AttributeError: 'PriceRange' object has no attribute '__dict__'
>>> 
>>> p.__slots__
('_low', '_high')
>>> 
>>> 
>>> p.extra = 5

Traceback (most recent call last):
  File "<pyshell#615>", line 1, in <module>
    p.extra = 5
AttributeError: 'PriceRange' object has no attribute 'extra'
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/properties.py ===========

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/properties.py", line 96, in <module>
    p = PriceRange(5, 10)
  File "/Users/mike/teaching/2017-04-24/properties.py", line 50, in __init__
    self.low = low
  File "/Users/mike/teaching/2017-04-24/properties.py", line 61, in low
    if value > self.high:
  File "/Users/mike/teaching/2017-04-24/properties.py", line 67, in high
    return self._high
AttributeError: _high
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/properties.py ===========
PriceRange(5, 10)
7.5
>>> PriceRange(5, 10)
PriceRange(5, 10)
>>> PriceRange(10, 5)

Traceback (most recent call last):
  File "<pyshell#617>", line 1, in <module>
    PriceRange(10, 5)
  File "/Users/mike/teaching/2017-04-24/properties.py", line 51, in __init__
    self.high = high
  File "/Users/mike/teaching/2017-04-24/properties.py", line 74, in high
    raise ValueError('Cannot be lesser than the low value')
ValueError: Cannot be lesser than the low value
>>> 
>>> 
>>> self.high

Traceback (most recent call last):
  File "<pyshell#620>", line 1, in <module>
    self.high
NameError: name 'self' is not defined
>>> p.high
10
>>> getattr(p, 'high')
10
>>> getattr(p, 'high'. 0)
SyntaxError: invalid syntax
>>> getattr(p, 'high', 0)
10
>>> getattr(p, 'foo', 0)
0
>>> p.foo

Traceback (most recent call last):
  File "<pyshell#626>", line 1, in <module>
    p.foo
AttributeError: 'PriceRange' object has no attribute 'foo'
>>> try:
	p.foo
except AttributeError:
	0

	
0
>>> getattr
<built-in function getattr>
>>> len
<built-in function len>
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
[('the', 1099), ('and', 900), ('to', 753), ('of', 658)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
>>> import dis
>>> dis.dis(foo)
 26           0 LOAD_CONST               0 (None)
              3 RETURN_VALUE        
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/racing.py", line 40, in <module>
    producer()
TypeError: producer() takes exactly 1 argument (0 given)
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[]
>>> counts.most_common(3)
[]
>>> counts.most_common(3)
[]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
[('the', 5), ('and', 2), ('soldiers', 2)]
>>> counts.most_common(3)
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[('the', 2198), ('and', 1800), ('to', 1506)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
Exception in thread Thread-5:
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py", line 801, in __bootstrap_inner
    self.run()
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py", line 754, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/Users/mike/teaching/2017-04-24/racing.py", line 48, in consumer
    word = q.pop()
IndexError: pop from empty list

PARALLEL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[('the', 1099), ('and', 900), ('to', 750)]
>>> counts.most_common(3)
[('the', 1099), ('and', 900), ('to', 750)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[('the', 844), ('and', 741), ('to', 633)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/racing.py =============
SERIAL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
PARALLEL VERSION
[('the', 1099), ('and', 900), ('to', 753)]
>>> 
