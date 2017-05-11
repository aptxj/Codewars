'''
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
'''

##############
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i


###############
import operator

def find_it(xs):
    return reduce(operator.xor, xs)


################
from collections import Counter
def find_it(l):
    return [k for k, v in Counter(l).items() if v % 2 != 0][0]


################
def find_it(seq):
    result = 0
    for x in seq:
        result ^= x
    return result


###################
def find_it(seq):
    nums = set()
    for num in seq:
        if num in nums:
            nums.remove(num)
        else:
            nums.add(num)
    return nums.pop()


###################
from itertools import groupby

def find_it(seq):
    return next(k for k, g in groupby(sorted(seq)) if len(list(g)) % 2)


###################
ef find_it(seq):
    return next(iter([x for x in seq if seq.count(x)%2==1]))


##################
def find_it(seq):
    odds = set()
    for i in seq:
        odds.symmetric_difference_update(set([i]))
    return odds.pop()



#################
find_it = lambda seq: [x for x in seq if seq.count(x)%2][0]


################
def find_it(seq):
    freq = {}
    for i in seq:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    for i in freq:
        if freq[i] % 2 != 0:
            return i


