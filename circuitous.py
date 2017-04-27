''' Copyright (c) 2017 Circuitous, Inc.

Eric Ries, "Lean Startup Method".
Agile : Waterfall :: Lean Startup : Business Plan
Build an MVP, then talk to customers.
"Get out of the building"

YAGNI: Ya ain't gonna need it.


Classes are for SHARED information
instances are for UNIQUE information

bound method            instance.method()
    regular method call
    implicitly passes the instance as the first arg

unbound method          Class.method(instance)
    calling a method from the class
    must explicitly pass the instance as the first arg

static method           Class.method()
    method called from the class
    does not require an instance, implictly nor explicitly

class method            Class.method()
    implictly receives the class obj as first arg
    useful for alternate constructors

name mangling           self.__name --> obj._Class__name
    for keeping an extra reference to internal dependencies

property
    looks like a normal attribute, but
    dispatches to a getter and setter instead


Liskov substitution principle
    a child should be substitable for the parent in all situations

Open/closed principle
    open for extension and closed for modification
    overrides should have no surprises/side-effects
'''

from collections import namedtuple
import math

Version = namedtuple('Version', 'major minor patch')


class Circle(object):
    'an advanced circle analytics toolkit'

    version = Version(0, 3, 2)

    def __init__(self, radius):
        'very few people read docstrings on magic methods'
        self.radius = radius

    @property
    def radius(self):
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0

    # radius = property(get_radius, set_radius)

    @classmethod
    def from_bbd(cls, diagonal):
        'Construct a new Circle from bounding box diagonal'
        radius = diagonal / math.sqrt(2)
        return cls(radius)

    def __repr__(self):
        # 'Circle(%r)' % (self.radius,)
        fmt = '{}(radius={!r})'
        return fmt.format(self.__class__.__name__, self.radius)

    def area(self):
        'Quadrature on a planar shape of uniform revolution'
        radius = self.__circumference() / math.pi / 2.0
        return math.pi * radius ** 2

    def circumference(self):
        'Perimeter of a circle'
        return math.pi * self.radius * 2

    __circumference = circumference

    @staticmethod
    def angle_to_grade(angle):
        '''
        Convert an inclinometer reading in degrees
        to a percent-grade.
        '''
        return math.tan(math.radians(angle)) * 100.0
