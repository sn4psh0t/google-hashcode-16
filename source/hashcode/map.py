import Point from point

class Map:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, pointStart, pointEnd):
         return sqrt(abs(pointStart.row - pointEnd.row)^2 - abs(pointStart.column - pointEnd.column)^2)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
