# -*- coding: utf-8 -*-

import sys
import os
import hashcode
from hashcode.warehouse import Warehouse
from hashcode.point import Point
from hashcode.product import Product
from hashcode.order import Order

from lib2to3.fixer_util import in_special_context

from hashcode import Battleship

def parseInputFile(inputFile):
    print ("*************************************************")
    print ("Results for input file " + inputFile)
    indexLine = 0
    orders = []
    wareHouses = []
    with open(inputFile, 'r') as f:
        for line in f:
            if indexLine == 0:
                line = line.rstrip('\n')
                currentLine = line.split(" ")
                rows = currentLine[0]
                columns = currentLine[1]
                dronesNumber = currentLine[2]
                turns = currentLine[3]
                payload = currentLine[4]
                indexLine = indexLine + 1
                line = next(f)
            if indexLine == 1:
                productTypes = int(line)
                indexLine = indexLine + 1
                line = next(f).rstrip('\n')
            if indexLine == 2:
                productTypesWeight = line.split(" ")
                indexLine = indexLine + 1
                line = next(f).rstrip('\n')
            if indexLine == 3:
                numberWarehouse = int(line)
                indexLine = indexLine + 1
                line = next(f).rstrip('\n')
            if indexLine == 4:
                for i in range (0,numberWarehouse):
                    currentLine = line.split(" ")
                    position = Point(currentLine[0], currentLine[1])
                    line = next(f).rstrip('\n')
                    currentLine = line.split(" ")
                    products = []
                    for j in range (0,productTypes):
                        products.append(Product(j, productTypesWeight[j]))
                    wareHouses.append(Warehouse(products, position))
                    indexLine = indexLine + 2
                    line = next(f).rstrip('\n')
            if indexLine == 4 + (2*numberWarehouse):
                # number of ordes
                numberOfOrders = int(line)
                indexLine = indexLine + 1
                line = next(f).rstrip('\n')
            if indexLine == 4 + (2*numberWarehouse) + 1:
                # begin orders
                for k in range (0, numberOfOrders):
                    orderPosition = line.split(" ")
                    line = next(f).rstrip('\n') # number of items in order
                    orderNumberOfProducts = int(line)
                    line = next(f).rstrip('\n') # items of products types
                    productTypesItems = line.split(" ")
                    productsForOrder = []
                    for i in range(0, orderNumberOfProducts):
                        productsForOrder.append(Product(productTypesItems[i], productTypesWeight[i]))
                    orders.append(Order(productsForOrder, Point(orderPosition[0], orderPosition[1])))
                    try:
                        line = next(f).rstrip('\n')
                    except StopIteration:
                        break

    print ("Map size " + str(rows) + " x " + str(columns))
    print ("Number of drones: " + dronesNumber)
    print ("Number of turns: " + turns)
    print ("Maximum Payload: " + payload)
    print ("Product types " + str(productTypes))
    print ("Product weights array length: " + str(len(productTypesWeight)))
    print ("Number of orders " + str(len(orders)))
    print ("Number of warehouses " + str(len(wareHouses)))
    print ("*************************************************\n")


if __name__ == '__main__':
    inputfile = os.path.dirname(__file__)
    inputfile = os.path.join(inputfile, '..', 'mother_of_all_warehouses.in')
    inputfile = os.path.abspath(inputfile)
    inputfile2 = os.path.dirname(__file__)
    inputfile2 = os.path.join(inputfile2, '..', 'busy_day.in')
    inputfile2 = os.path.abspath(inputfile2)
    inputfile3 = os.path.dirname(__file__)
    inputfile3 = os.path.join(inputfile3, '..', 'redundancy.in')
    inputfile3 = os.path.abspath(inputfile3)

    inputs = [ inputfile, inputfile2, inputfile3 ]

    if len(sys.argv) > 1:
        inputs = sys.argv[1:]

    for f in inputs:
        if not os.path.isfile(f):
            f = os.path.join(os.getcwd(), f)
        parseInputFile(f)