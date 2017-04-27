'''
All about using properties.


1970s   Relational Databases

    PriceRange
    ================
    low         real
    high        real
    mid         real

    SELECT low, mid, high FROM PriceRange;


1980s   Normalized Databases

    PriceRange
    ================
    low         real
    high        real

    SELECT low, (low + high) / 2 as mid, high FROM PriceRange;


1990s   Table Views

    PriceRange
    ================
    low         real
    high        real

    PriceRangeView
    ================
    low         real
    high        real
    mid         low + high / 2

    SELECT low, mid, high FROM PriceRangeView;
'''

from __future__ import division
import validators

class PriceRange(object):

    __slots__ = ('_low', '_high')

    def __init__(self, low, high):
        self.low = low
        self.high = high

    @property
    def low(self):
        return self._low

    @low.setter
    def low(self, value):
        validators.is_number(value)
        validators.is_positive(value)
        if value > getattr(self, 'high', float('inf')):
            raise ValueError('Cannot be greater than the high value')
        self._low = value

    @property
    def high(self):
        return self._high

    @high.setter
    def high(self, value):
        validators.is_number(value)
        validators.is_positive(value)
        if value < getattr(self, 'low', float('-inf')):
            raise ValueError('Cannot be lesser than the low value')
        self._high = value

    @property
    def mid(self):
        'Halfway between the low and the high'
        return (self.low + self.high) / 2

    def recenter_around_mid(self, mid):
        '''
        Recenter around a new mid-point, keeping the same
        distance between the high and the low.
        '''
        distance = (self.high - self.low) / 2
        self.low = mid - distance
        self.high = mid + distance

    def __repr__(self):
        return '%s(%r, %r)' % (type(self).__name__, self.low, self.high)


if __name__ == '__main__':
    p = PriceRange(5, 10)
    print p
    print p.mid
