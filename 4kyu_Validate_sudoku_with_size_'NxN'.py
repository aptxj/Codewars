'''
Given a Sudoku data structure with size NxN, N > 0 and √N == integer, write a method to validate if it has been filled out correctly.

The data structure is a multi-dimensional Array(in Rust: Vec<Vec<u32>>) , ie:

[
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],

  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],

  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
]
Rules for validation

Data structure dimension: NxN where N > 0 and √N == integer
Rows may only contain integers: 1..N (N included)
Columns may only contain integers: 1..N (N included)
'Little squares' (3x3 in example above) may also only contain integers: 1..N (N included)
'''




#######################
import math

class Sudoku(object):
    def __init__(self, board):
        self.board = board

    def is_valid(self):
        if not isinstance(self.board, list):
            return False
        n = len(self.board)
        rootN = int(round(math.sqrt(n)))
        if rootN * rootN != n:
            return False
        isValidRow = lambda r : (isinstance(r, list) and
                                 len(r) == n and
                                 all(map(lambda x : type(x) == int, r)))
        if not all(map(isValidRow, self.board)):
            return False
        oneToN = set(range(1, n + 1))
        isOneToN = lambda l : set(l) == oneToN
        tranpose = [[self.board[j][i] for i in range(n)] for j in range(n)]
        squares = [[self.board[p+x][q+y] for x in range(rootN)
                                         for y in range(rootN)]
                                         for p in range(0, n, rootN)
                                         for q in range(0, n, rootN)]
        return (all(map(isOneToN, self.board)) and
                all(map(isOneToN, tranpose)) and
                all(map(isOneToN, squares)))




##########################
import numpy as np
class Sudoku(object):

    def __init__(self, theArray):
        self.grid = np.array(theArray)
        self.listgrid = theArray

        self.N = len(theArray)
        self.M = len(theArray[0])

    def has_valid_size(self):

        if isinstance(self.listgrid[0][0], bool): return False
        if self.grid.shape == (1,1):
            return True
        for i in self.listgrid:
            if len(i) != self.N: return False
        return True


    #your code here
    def is_valid(self):
        if not self.has_valid_size():
            return False

        seqs2check = [self.getRowsIterator(), self.getColsIterator(), self.getSquaresIterator()]
        for it in seqs2check:
            for seq in it:
                if self.checkSeq(seq) == False:
                    return False
        return True

    def getRowsIterator(self):
        for i in range(self.N):
            yield self.grid[i,:]

    def getColsIterator(self):
        for i in range(self.N):
            yield self.grid[:,i]

    def getSquaresIterator(self):
        squareSize = int(np.sqrt(self.N))
        for i in range(squareSize):
            for j in range(squareSize):
                ix1 = i*squareSize
                ix2 = j*squareSize
                yield self.grid[ix1:ix1+squareSize, ix2:ix2+squareSize].flatten()

    def checkSeq(self, seq):
        return sorted(seq) == range(1,self.N+1)





#########################
import math

class Sudoku(object):
    def __init__(self, board):
        self.board = board

    def is_valid(self):
        if not isinstance(self.board, list):
            return False
        n = len(self.board)
        rootN = int(round(math.sqrt(n)))
        if rootN * rootN != n:
            return False
        isValidRow = lambda r : (isinstance(r, list) and
                                 len(r) == n and
                                 all(map(lambda x : type(x) == int, r)))
        if not all(map(isValidRow, self.board)):
            return False
        oneToN = set(range(1, n + 1))
        isOneToN = lambda l : set(l) == oneToN
        tranpose = [[self.board[i][j] for i in range(n)] for j in range(n)]
        squares = [[self.board[p+x][q+y] for x in range(rootN)
                                         for y in range(rootN)]
                                         for p in range(0, n, rootN)
                                         for q in range(0, n, rootN)]
        return (all(map(isOneToN, self.board)) and
                all(map(isOneToN, tranpose)) and
                all(map(isOneToN, squares)))





#######################
