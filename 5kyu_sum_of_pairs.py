"""
https://www.codewars.com/kata/54d81488b981293527000c8f
Sum of Pairs
Given a list of integers and a single sum value,
return the first two values (parse from the left please) in order of appearance that add up to form the sum.
sum_pairs([11, 3, 7, 5],         10)
#              ^--^      3 + 7 = 10
== [3, 7]
sum_pairs([4, 3, 2, 3, 4],         6)
#          ^-----^         4 + 2 = 6, indices: 0, 2 *
#             ^-----^      3 + 3 = 6, indices: 1, 3
#                ^-----^   2 + 4 = 6, indices: 2, 4
#  * entire pair is earlier, and therefore is the correct answer
== [4, 2]
sum_pairs([0, 0, -2, 3], 2)
#  there are no pairs of values that can be added to produce 2.
== None/nil/undefined (Based on the language)
sum_pairs([10, 5, 2, 3, 7, 5],         10)
#              ^-----------^   5 + 5 = 10, indices: 1, 5
#                    ^--^      3 + 7 = 10, indices: 3, 4 *
#  * entire pair is earlier, and therefore is the correct answer
== [3, 7]
Negative numbers and duplicate numbers can and will appear.
NOTE: There will also be lists tested of lengths upwards of 10,000,000 elements.
Be sure your code doesn't time out.
"""

def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)

def sum_pairs(ints, s):
    d = set()
    for n in ints:
        if n in d: return [s - n, n]
        d.add(s - n)

def sum_pairs(ints, s):
    bla = set()
    try: return filter(lambda x: x != None ,[[s-x, x] if s-x in bla else bla.add(x) for x in ints])[0]
    except: return None

def sum_pairs(ints, s):
    prev_num = None
    for i in range(len(ints)):
      if ints[i] == prev_num:
          continue
      prev_num = ints[i]
      counter = i
      while counter != 0:
        counter -= 1
        if ints[i] + ints[counter] == s:
          return [ints[counter], ints[i]]

def sum_pairs(ints, s):
    t = {ints[0]:True}
    for i, n in enumerate(ints[1:]):
        if s-n in t:
            return [s-n, n]
        t[n] = True

def sum_pairs(ints, s):
    sol_dict = {}
    for j in ints:
        if (s - j, j) in sol_dict:
            return ([s - j, j])
        else:
            sol_dict[(j, s - j)] = [j, s - j]
    else:
        return None

def sum_pairs(ints, s):
  x = {}
  for i in ints:
    if i in x.keys():
      return [x[i],i]
    else:
      x[s-i] = i
  return None

def sum_pairs(ints, s):
    """
    left to right, intuitive
    """
    rng = list(range(len(ints)))
    for i in rng[1:]:
        int2expect = s - ints[i]
        for j in rng[:i]:
            if ints[j] == int2expect:
                return [int2expect, ints[i]]

def sum_pairs(ints, s):
    """
    right to left, intuitive
    """
    ret = []
    rng = list(range(len(ints)))
    for i in rng[::-1]:
        int2expect = s - ints[i]
        for j in rng[:i]:
            if ints[j] == int2expect:
                ret = [int2expect, ints[i]]
    if ret:
        return ret

def sum_pairs(ints, s):
    """
    searched cache by dict(hashed)
    """
    ints_dict = {}
    for i in range(len(ints)):
        int2expect = s - ints[i]
        if int2expect in ints_dict:
            return [int2expect, ints[i]]
        ints_dict[ints[i]] = None

def sum_pairs(ints, s):
    """
    searched cache by set(hashed)
    """
    ints_set = set()
    for i in range(len(ints)):
        int2expect = s - ints[i]
        if int2expect in ints_set:
            return [int2expect, ints[i]]
        ints_set.add(ints[i])

def sum_pairs(ints, s):
    """
    searched cache by list
    """
    ints_set = []
    for i in range(len(ints)):
        int2expect = s - ints[i]
        if int2expect in ints_set:
            return [int2expect, ints[i]]
        ints_set.append(ints[i])

def sum_pairs(ints, s):
    """
    itertools.combinations
    """
    for int_02, int_01 in list(itertools.combinations(ints[::-1], 2))[::-1]:
        if int_02 + int_01 == s:
            return [int_01, int_02]
