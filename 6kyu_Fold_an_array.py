'''
#Fold an array

In this kata you have to write a method that folds a given array of integers by the middle x-times.

An example says more than thousand words:

Fold 1-times:
[1,2,3,4,5] -> [6,6,3]

A little visualization (NOT for the algorithm but for the idea of folding):

 Step 1         Step 2        Step 3       Step 4       Step5
                     5/           5|         5\
                    4/            4|          4\
1 2 3 4 5      1 2 3/         1 2 3|       1 2 3\       6 6 3
----*----      ----*          ----*        ----*        ----*


Fold 2-times:
[1,2,3,4,5] -> [9,6]
'''


###############
def fold_array(array, runs):
    result = array[:]
    #result = list(array)
    #*result, = array
    #import copy
    #result = copy.copy(array)
    #result = copy.deepcopy(array)
    for _ in range(runs):
        if len(result)%2 == 0:
            for i in range(1,len(result)/2+1):
                result.append(result.pop(0) + result.pop(-i))
        else:
            for i in range(1, len(result)//2 +1):
                result.append(result.pop(0) + result.pop(-i))
            result.append(result.pop(0))
    return result



#############
def fold_array(array, runs):
    nums = list(array)
    for _ in xrange(runs):
        for a in xrange(len(nums) // 2):
            nums[a] += nums.pop()
    return nums

###############
from functools import reduce

def fold_array(array, runs):
    if runs == 0:
        return array
    else:
        return fold_array(fold(array), runs - 1)


def fold(array):
    mid = len(array) // 2
    if len(array) % 2 == 0:
        return [reduce(lambda a, b: a + b, pair)
                for pair in list(zip(array[:mid], array[::-1][:mid]))]
    else:
        return fold(array[:mid] + array[(mid + 1):]) + [array[mid]]



#################
def fold_array(arr, runs):
    center, mod = divmod(len(arr), 2)
    arr_left = arr[:center]
    arr_right = arr[center+mod:]
    tail = [arr[center]] * mod
    folded = [sum(i) for i in zip(arr_left, arr_right[::-1])] + tail
    return folded if runs == 1 else fold_array(folded, runs - 1)


###################
def fold_array(arr, runs):
  from math import ceil

  if runs < 1 or len(arr) < 2:
    return arr

  t = len(arr) // 2
  p = int(ceil(len(arr) / 2))

  folded = arr[:p]

  for i in range(t):
    folded[i] += arr[-i-1]

  return fold_array(folded, runs-1)


#####################
from itertools import zip_longest
from functools import reduce
def fold_array(array, runs):
    f = lambda x, y: [a + b for a, b in zip_longest(x[:len(x)//2], reversed(x[len(x)//2:]), fillvalue=0)]
    return reduce(f, range(runs), array)



#####################
def fold(arr):
    length = len(arr)
    mid = length // 2
    return [a + b for a, b in zip(arr, arr[-1:-mid-1:-1])] + [arr[mid]] * (length & 1)

def fold_array(array, runs):
    ret = array
    for __ in range(runs):
        ret = fold(ret)
    return ret



########################
def fold_array(array, runs):
    for _ in range(runs):
        r = array[(len(array)+1)//2:][::-1]
        array = array[:(len(array)+1)//2]
        for i in range(len(r)):
            array[i] += r[i]
    return array


#####################
def my_add(a,b):
    if a is None:
        return b
    if b is None:
        return a
    return a+b

def fold_array(arr, runs):
    if runs == 0:
        return arr
    half = len(arr) // 2
    front, end = arr[:half], list(reversed(arr[half:]))
    arr = list(map(my_add, front, end)) if half else arr
    return fold_array(arr, runs-1)


############
def fold_array(array, runs):
        new_array = []
        new_array.extend(array)
        for i in range(runs):
                if len(new_array)==1:
                        break
                else:
                    for j in range(len(new_array)//2):
                        new_array[j]=new_array[j]+new_array[-1-j]
                if len(new_array)%2 != 0:
                    new_array[j+2:]=[]
                else:
                    new_array[j+1:]=[]
        return(new_array)



#################
def fold_array(arr, runs):
    array = arr[:]
    for i in range(runs):
        if len(array) == 1:
            return array
        half = len(array)/ 2
        for j in range(half):
            array[j] += array[-(j+1)]
        array = array[:-half]
    return array



##################
def fold_array(array, runs):
    a = array[:]
    for n in range(runs):
        l = len(a) // 2
        r = len(a) % 2
        for i in range(l):
            a[i] = a[i] + a[len(a) - i - 1]
        a = a[:l + r]
    return a


###############
def fold_array(arr, runs):
    array=[i for i in arr]
    if runs == 0: return array
    length = len(array)
    for i in range(length//2):
        array[i]+=array[-i-1]
    return fold_array(array[:length//2+length%2],runs-1)



