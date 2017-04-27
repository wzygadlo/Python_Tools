'''
Tracking down race conditions in multithreaded code.
(The easy way using multiprocessing.pool.ThreadPool)

Race conditions:
1. The consumer can race ahead of the producer
    and accidentally early-exit before the producer is finished.

    Fix: delay before starting the consumer
    Better Fix: "join" the producers before "join"ing the queue

2. The main thread can race ahead of the subthreads
    and print the results before the subthreads are finished.

    Fix: wait until the producer and consumer are dead.

3. The consumer threads can race against each other
    and LBYL pop from an empty queue.

    Fix: use EAFP to ensure getting a word is an atomic action

4. The consumer threads can race against each other
    and lose information during the counting get/set two-step

    Fix: lock the shared resource (counts) while using it
'''

from collections import Counter
import re

counts = Counter()
with open('data/dialogue.txt') as f:
    for line in f:
        for word in re.findall(r'[a-z]+', line.lower()):
            counts[word] += 1

print 'SERIAL VERSION'
print counts.most_common(3)

########################################
# Multi-threading

from collections import Counter
from threading import Thread, Lock
from Queue import Queue
import re

q = Queue()
counts = Counter()
counts_lock = Lock()

def producer(filename):
    with open(filename) as f:
        for line in f:
            for word in re.findall(r'[a-z]+', line.lower()):
                q.put(word)

def consumer():
    while True:
        word = q.get()
        with counts_lock:
            counts[word] += 1
        q.task_done()

if __name__ == '__main__':
    filenames = ['data/dialogue.txt']
    
    producers = []
    for filename in filenames:
        t = Thread(target=producer, args=(filename,))
        t.start()
        producers.append(t)

    consumers = []
    for i in range(10):
        t = Thread(target=consumer)
        t.daemon = True
        t.start()
        consumers.append(t)

    for t in producers:
        t.join()
    q.join()

    print 'PARALLEL VERSION'
    print counts.most_common(3)
