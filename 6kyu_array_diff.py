
"""
Your goal in this kata is to implement an difference function,
which subtracts one list from another.
It should remove all values from list a, which are present in list b.
difference([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must
be removed from the other:
difference([1,2,2,2,3],[2]) == [1,3]
"""


def array_diff(a, b):
    return [x for x in a if x not in b]


def array_diff(a, b):
    #your code here
    for i in range(len(b)):
        while b[i] in a:
            a.remove(b[i])
    return a


def array_diff(a, b):
  for el in b:
    while el in a:
      a.remove(el)
  return a


def array_diff(a, b):
    for x in b:
        while a.count(x) != 0:
            a.remove(x)
    return a


def array_diff(a, b):
    c = []
    for e in a:
        for e2 in b:
            if e == e2: break
        	else: c.append(e)
    return c


def array_diff(a, b):
    clist=[]
    for x in a:
        if x in b:continue
        clist.append(x)
    return clist


def array_diff(a, b):
    c = []
    for i in a:
        flag = 0
        for j in b:
            if i == j:
                flag = 1
                break
        if flag == 0:
            c.append(i)
    return c


def array_diff(a, b):
	return list(filter(lambda x: x not in b, a))


def array_diff(a, b):
    new_list = []
    for i in a:
        if i not in b:
            new_list += [i]
    return new_list


