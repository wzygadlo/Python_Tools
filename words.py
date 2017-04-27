'''
An analysis of the dialogue in "Hamlet".
'''

# Task 1: Show the 3 most common words

from collections import Counter

counts = Counter()
with open('data/dialogue.txt') as f:
    for line in f:
        for word in line.split():
            counts[word] += 1

counts.most_common(3)


# Task 2: Organize the unique words by first letter

from collections import defaultdict

words = defaultdict(set)
with open('data/dialogue.txt') as f:
    for line in f:
        for word in line.split():
            initial = word[0]
            words[initial].add(word)

# Task 3
# word --> list of words that follow

from collections import defaultdict
import random

def train(filename, size=1):
    chain = defaultdict(list)
    last = (None,) * size
    with open(filename) as f:
        for line in f:
            for word in line.split():
                chain[last].append(word)
                last = last[1:] + (word,)
    return chain

def walk(chain):
    last = random.choice(list(chain))
    for word in last:
        print word,
    while word[-1] not in '.?!':
        word = random.choice(chain[last])
        print word,
        last = last[1:] + (word,)

def randomness(chain):
    n = sum(len(set(options)) > 1
            for options in chain.values())
    return float(n) / len(chain)

if __name__ == '__main__':
    chain = train('data/dialogue.txt', 2)
    walk(chain)
