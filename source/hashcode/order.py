from .product import Product
from .point import Point

class Order:
    def __init__(self, products, position):
        self.products = products
        self.position = position
        self.delivered = False
        self.deliveredProducts = []

    
        

    
