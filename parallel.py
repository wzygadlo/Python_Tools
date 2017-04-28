'''
parallelism
'''

import time, random, itertools
from multiprocessing.pool import ThreadPool
from multiprocessing import Pool, cpu_count
from threading import Lock

# import numpy

def io_bound(x):
    'simulate an input/output-constrained task'
    time.sleep(random.uniform(0, 2))
    return x + 1

def cpu_bound(x):
    'a compute-constrained task'
    sum(xrange(int(1e6)))
    # numpy.sum(numpy.arange(1e6, dtype='int'))
    return x + 1

count = 0

def racing(x):
    global count
    count += 1
    return x

def tick(x, lock=Lock()):
    global count
    with lock:
        count += 1
    return x

def serial(func, n):
    for result in itertools.imap(func, range(n)):
        print result

def threaded(func, n, maxthreads=25):
    pool = ThreadPool(min(n, maxthreads))
    for result in pool.imap_unordered(func, range(n)):
        print result

def multiproc(func, n, maxprocs=cpu_count()):
    pool = Pool(min(n, maxprocs))
    for result in pool.imap_unordered(func, range(n)):
        print result

if __name__ == '__main__':
    start = time.time()
    threaded(io_bound, 10)
    stop = time.time()
    print 'DURATION %.2f' % (stop - start)
