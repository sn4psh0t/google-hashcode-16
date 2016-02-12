# -*- coding: utf-8 -*-
from .product import Product
from .point import Point

class Warehouse:
    def __init__(self, products, position):
        self.products = products
        self.position = position

    def compare(self, order):
        pass