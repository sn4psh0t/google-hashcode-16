#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from hashcode import Battleship

if __name__ == '__main__':
        inputfile = os.path.dirname(__file__)
        inputfile = os.path.join(inputfile, '..', 'input.in')
        inputfile = os.path.abspath(inputfile)

        inputs = [ inputfile ]

        if len(sys.argv) > 1:
                inputs = sys.argv[1:]

        for f in inputs:
                if not os.path.isfile(f):
                        f = os.path.join(os.getcwd(), f)
                Battleship(f).go()
