'''
Our customers' code.
'''

from circuitous import Circle
from random import random, seed

# Customer 0: Our academic friends

print 'A proposal to research the areas of circles'
print 'with Circuitous(tm)', Circle.version
n = 5
seed(42)
circles = (Circle(random()) for i in xrange(n))
areas = (c.area() for c in circles)
print 'The average area of', n, 'random circles'
print 'seeded with the Answer to Life and Everything'
print 'is', sum(areas) / n
print

# Customer 1: Local rubber sheet company

cuts = [0.7, 0.3, 0.5]
circles = [Circle(radius) for radius in cuts]
for c in circles:
    print 'A circle with radius', c.radius
    print 'has a cold area %.2f' % c.area()
    print 'and a perimeter {:.2f}'.format(c.circumference())
    c.radius *= 1.1
    # c.set_radius(c.get_radius() * 1.1)
    print 'and a warm area %.2f' % c.area()
    print

# Customer 2: Regional tyre company

class Tyre(Circle):

##    def __init__(self, radius, pressure):
##        Circle.__init__(self, radius)
##        self.pressure = pressure

    def circumference(self):
        'adjusted perimeter for width of tyre'
        return 1.25 * Circle.circumference(self)

t = Tyre(22)
print 'a tire of radius', 22
print 'has an area %.2f' % t.area()
print 'and a circumference %.2f' % t.circumference()

# Customer 3: National trucking company

print 'a hill of with 7 degree incline is a'
print '%d%% grade' % Circle.angle_to_grade(7)
print

# Customer 4: International graphics company
# We have money and power!
# We build circles NOT with radius
# but with a bounding box diagonal

c = Circle.from_bbd(10)
print 'a circle with bounding box diagonal 10'
print 'has a radius %.2f' % c.radius
print 'and an area %.2f' % c.area()
print

# Customer 5: the government
# We like to micromanage
# we'll tell you not just WHAT to build
# but also HOW to build it

# ISO-12345-fake
# Thou shalt not directly access the radius
# inside area methods. Area methods must
# infer the radius from the circumference.

# ISO-12346
# Circle instances must not store the radius.
# A circle instance must store the diameter
# and ONLY the diameter.

print 'government inspection'
c = Circle(10)
print c.__dict__
print c.radius
print c.area()
c.radius = 20
print c.__dict__

