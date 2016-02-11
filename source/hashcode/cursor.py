# -*- coding: utf-8 -*-

class Cursor:
        def __init__(self, matrix, row=0, col=0):
                self.matrix = matrix
                self.move(row, col)

        def clone(self):
                return Cursor(self.matrix, self.row, self.col)

        def move(self, row, col):
                self.row = row
                self.col = col
                return self.matrix.get(row, col)

        def next(self):
                lastrow = self.matrix.rows - 1
                lastcol = self.matrix.cols - 1
                if self.col < lastcol:
                        self.col += 1
                elif self.row < lastrow:
                        self.row += 1
                        self.col = 0
                else:
                        return None
                return self.matrix.get(self.row, self.col)

        def current(self):
                return self.matrix.get(self.row, self.col)

        def left(self):
                if self.col == 0:
                        return None
                self.col -= 1
                return self.matrix.get(self.row, self.col)

        def right(self):
                if self.col == (self.matrix.cols - 1):
                        return None
                self.col += 1
                return self.matrix.get(self.row, self.col)

        def up(self):
                if self.row == 0:
                        return None
                self.row -= 1
                return self.matrix.get(self.row, self.col)

        def down(self):
                if self.row == (self.matrix.rows - 1):
                        return None
                self.row += 1
                return self.matrix.get(self.row, self.col)

