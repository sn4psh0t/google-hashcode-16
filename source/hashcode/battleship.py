# -*- coding: utf-8 -*-

from .matrix  import loadmatrix, savematrix

class Battleship:
        def __init__(self, file):
                self.file = file
                self.matrix  = loadmatrix(file)
                self.matrixfile = file + '-matrix.txt'

        def go(self):
                savematrix(self.matrixfile, self.matrix)
