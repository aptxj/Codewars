'''
This problem takes its name by arguably the most important event in the life of the ancient historian Josephus: according to his tale, he and his 40 soldiers were trapped in a cave by the Romans during a siege.

Refusing to surrender to the enemy, they instead opted for mass suicide, with a twist: they formed a circle and proceeded to kill one man every three, until one last man was left (and that it was supposed to kill himself to end the act).

Well, Josephus and another man were the last two and, as we now know every detail of the story, you may have correctly guessed that they didn't exactly follow through the original idea.

You are now to create a function that returns a Josephus permutation, taking as parameters the initial array/list of items to be permuted as if they were in a circle and counted out every k places until none remained.

Tips and notes: it helps to start counting from 1 up to n, instead of the usual range 0..n-1; k will always be >=1.

For example, with n=7 and k=3 josephus(7,3) should act this way.

[1,2,3,4,5,6,7] - initial sequence
[1,2,4,5,6,7] => 3 is counted out and goes into the result [3]
[1,2,4,5,7] => 6 is counted out and goes into the result [3,6]
[1,4,5,7] => 2 is counted out and goes into the result [3,6,2]
[1,4,5] => 7 is counted out and goes into the result [3,6,2,7]
[1,4] => 5 is counted out and goes into the result [3,6,2,7,5]
[4] => 1 is counted out and goes into the result [3,6,2,7,5,1]
[] => 4 is counted out and goes into the result [3,6,2,7,5,1,4]
So our final result is:

josephus([1,2,3,4,5,6,7],3)==[3,6,2,7,5,1,4]
'''

###########################
def josephus(xs, k):
    i, ys = 0, []
    while len(xs) > 0:
        i = (i + k - 1) % len(xs)
        ys.append(xs.pop(i))
    return ys


###########################
def josephus(items,k):
  if len(items)==0: return []
  if len(items)==1: return [items[0]]
  i = ((k-1)%len(items))
  return [items[i]] + josephus(items[i+1:]+items[:i], k)


############################
def josephus(items, k):
    """
    recombine, recursion, global update
    """
    ret = []

    def recur(items):
        n = len(items)
        if n == 0:
            return
        i = (k - 1) % n
        ret.append(items[i])
        recur(items[i + 1:] + items[:i])

    recur(items)

    return ret



###############################
def josephus(items, k):
    """
    recombine, loop
    """
    ret = []

    n = len(items)
    for n in range(n, 0, -1):
        i = (k - 1) % n
        ret.append(items[i])
        items = items[i + 1:] + items[:i]

    return ret



#################################
def josephus(items, k):
    """
    deque.rotate deque.popleft
    """
    items = deque(items)
    ret = []
    while items:
        items.rotate(1 - k)
        ret.append(items.popleft())
    return ret




###############################
def josephus(items, k):
    """
    very basic
    """
    ret = []
    n = len(items)
    i = 0
    i_old = 0
    i_add = 0
    i_lst = []
    for _ in range(n):
        f, i = divmod(i + k - 1, n)
        if f == 0:
            i_add = sum([i_old <= i_ <= i for i_ in i_lst])
        elif f == 1:
            i_add = sum([i_old <= i_ for i_ in i_lst]) + sum([i_ <= i for i_ in i_lst])
        elif f > 1:
            i_add = sum([i_old <= i_ for i_ in i_lst]) + sum([i_ <= i for i_ in i_lst]) + (f - 1) * len(i_lst)

        while i_add > 0:
            i = (i + 1) % n
            if i in i_lst:
                continue
            i_add -= 1

        i_lst.append(i)
        ret.append(items[i])
        i = (i + 1) % n
        i_old = i

    return ret
