'''
Enough is enough!

Alice and Bob were on a holiday. Both of them took many pictures of the places they've been, and now they want to show Charlie their entire collection. However, Charlie doesn't like this sessions, since the motive usually repeats. He isn't fond of seeing the Eiffel tower 40 times. He tells them that he will only sit during the session if they show the same motive at most N times. Luckily, Alice and Bob are able to encode the motive as a number. Can you help them to remove numbers such that their list contains each number only up to N times, without changing the order?

Task

Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].

Example

  delete_nth ([1,1,1,1],2) # return [1,1]

  delete_nth ([20,37,20,21],1) # return [20,37,21]
'''

##########
def delete_nth(order,max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans

#############
from collections import defaultdict

def delete_nth(order,max_e):
    c = defaultdict(int)
    def count(x):
        c[x] += 1
        return c[x] <= max_e
    return filter(count, order)


##############
def delete_nth(order, max_e):
    d = {}
    res = []
    for item in order:
      n = d.get(item, 0)
      if n < max_e:
        res.append(item)
        d[item] = n+1
    return res


##############
from collections import Counter

def delete_nth(order, max_e):
    c = Counter()
    result = []
    for element in order:
        if c[element] < max_e:
            c[element] += 1
            result.append(element)
    return result


###############
def delete_nth(order,max_e):
    return [order[i] for i in range(len(order)) if order[0:i+1].count(order[i]) <= max_e]


################
def delete_nth(order,max_e):
    return [o for i,o in enumerate(order) if order[:i].count(o)<max_e ]


##############
delete_nth = lambda order, max_e: [x for i, x in enumerate(order) if order[:i].count(x) < max_e]


###############
def delete_nth(order,max_e):
    for n in range(len(order)-1, -1, -1):
        if order.count(order[n]) > max_e: del order[n]
    return order


###############
def delete_nth(order,max_e):
    order = order[::-1]
    for x in order:
      while order.count(x) > max_e:
        order.pop(order.index(x))
    return order[::-1]


###############
def delete_nth(order,m):
    i = 0
    while i < len(order):
        if order[:i].count(order[i]) == m:
            order.pop(i)
            i -= 1
        i += 1
    return order


###############
def delete_nth(order,max_e):
    l=[]
    map(lambda x: l.append(x) if l.count(x) < max_e else False, order)
    return l

###############
def delete_nth(order,max_e):
    # code here
    tmp = []
    dic = dict(zip(set(order),[0.0] * len(set(order))))

    for w in order:
        dic[w] += 1

        if dic[w] <= max_e:
            tmp.append(w)
    return tmp

