'''
Meditate on classes and closures...

    "Objects are a poor man's closures.
     Closures are a poor man's objects." -- Qc Na

'''

count_a = 0
count_b = 0

def tick_a():
    global count_a
    count_a += 1
    print count_a

def tick_b():
    global count_b
    count_b += 1
    print count_b


### Solution: OOP

class Ticker:

    def __init__(self):
        self.count = 0
    
    def tick(self):
        self.count += 1
        print self.count

a = Ticker()
b = Ticker()

### Solution: Closures

def ticker():
    def tick():
        tick.count += 1
        print tick.count
    tick.count = 0
    return tick

tick_a = ticker()
tick_b = ticker()


