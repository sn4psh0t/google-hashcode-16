# -*- coding: utf-8 -*-

import time

class Matrix:
        def __init__(self, rows, cols, data=None):
                self.rows = rows
                self.cols = cols

                if data is None:
                        data = [ [0 for _ in range(cols)] for _ in range(rows) ]

                self.data = data

        def get(self, row, col):
                return self.data[row][col]

        def set(self, row, col, val):
                self.data[row][col] = val

class SyncMatrix:
        def __init__(self, matrix, syncfile):
                self.matrix   = matrix
                self.syncfile = syncfile

        def __getattr__(self, attr):
                return getattr(self.matrix, attr)

        def set(self, *args, **kargs):
                ret = self.matrix.set(*args, **kargs)
                savematrix(self.syncfile, self)
                return ret

def loadmatrix(file):
        with open(file, 'r') as f:
                line = next(f)
                line = line.split(' ')
                rows, cols = map(int, line)
                matrix = Matrix(rows, cols)

                for row, line in enumerate(f):
                        for col, char in enumerate(line):
                                if char == '#':
                                        matrix.set(row, col, 1)

                return matrix


def savematrix(file, matrix):
        with open(file, 'w') as f:
                for r in range(matrix.rows):
                        for c in range(matrix.cols):
                                v = str(matrix.get(r, c))
                                f.write(v)

                        f.write('\n')
