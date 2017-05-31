'''
Here you will create the classic pascal's triangle. Your function will be passed the depth of the triangle and you code has to return the corresponding pascal triangle upto that depth

The triangle should be returned as a nested array.

for example:

pascal(5) # should return [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
To build the triangle, start with a single 1 at the top, for each number in the next row you just take the two numbers above it and add them together (except for the edges, which are all "1"). eg

          [1]
        [1   1]
       [1  2  1]
      [1  3  3  1]
here you get the 3 by adding the 2 and 1 above it.
'''

#####################
def pascal(n):
    yang = []
    r = []
    for x in range(n):
        l = len(r)
        r = [1 if i == 0 or i == l else r[i-1]+r[i] for i in range(l+1)]
        yang.append(r)
    return yang



###################
def pascal(p):
    triangle = [[1]]
    for _ in range(p - 1):
        to_sum = zip([0] + triangle[-1], triangle[-1] + [0])
        triangle.append(map(sum, to_sum))
    return triangle



####################
def pascal(p):

    t = [[1]]

    for _ in range(2, p + 1):
        t.append([1] + [a + b for a, b in zip(t[-1][:-1], t[-1][1:])] + [1])

    return t


####################
def pascal(p):
    def create_row(n):
        row = [1]
        for k in range(n):
            row.append(row[k] * (n-k) / (k+1))
        return row
    tri = []
    for row in range(p):
        tri.append(create_row(row))
    return tri



####################
from operator import add
def pascal(p):
    tr = [[1]]
    for i in range(p-1):
        tr.append(map(add, [0]+tr[i], tr[i]+[0]))
    return tr



######################
from math import factorial
def pascal(p):
  return [[int((factorial(p)/(factorial(k)*factorial(p-k)))) for k in range(0,p+1)] for p in range(0,p)]



#######################
def pascal(p):
    if p == 1:
        return [[1]]
    res = [ [1], [1,1] ]
    for i in range(p-2):
        res.append( [1] + [res[-1][j] + res[-1][j+1] for j in range(len(res[-1]) - 1) ] + [1] )
    return res


##########################
def pascal(p):
    if p == 1: return [[1]]
    res = [[1], [1, 1]]
    p -= 2
    while p:
        res.append(
            [1] + [val+res[-1][pos+1]
                for pos, val
                    in list(enumerate(res[-1]))[:-1]] + [1]
        )
        p -= 1
    return res


#############################
pascal = lambda p: reduce(lambda t,_: t + [map(sum, zip([0]+t[-1], t[-1]+[0]))], range(1,p), [[1]])




##############################
def pascal(p):
    rows = [[1], [1, 1]]

    for _ in range(1, p):
        row = [1]
        lastRow = rows[-1]
        for j in range(len(lastRow) - 1):
            row += [sum(lastRow[j:j+2])]
        row += [1]
        rows += [row]

    return rows[:p]





