from point import Point
from product import Product
from order import Order

class Drone:
    def __init__(self, position, size, products):
        self.position = position
        self.size = size
        self.products = products

    def updatePosition(self, newPosition):
        self.position = newPosition

    def load(self, products):
        for product in products:
            self.products.append(product)

    def deliver(self, orders, products):
        for order in orders:
            if self.position != order.position:
                for product in products:
                    if product in order.products:
                        if (self.position != product.position):
                            # fly to new position
                            self.position = order.position
                            order.deliveredProducts.append(product
                        self.products.remove(product)

    

    def unload(self):
        pass
