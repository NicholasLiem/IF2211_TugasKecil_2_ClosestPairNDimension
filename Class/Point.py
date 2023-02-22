import math
import numpy as np

class Point:

    # coords adalah tuple yang isinya value koordinatnya
    # dimension adalah berapa jumlah dimensinya

    def __init__(self, *args):
        self.coords = args
        self.dimension = len(self.coords)

    def getCoords(self, index):
        return self.coords[index]
    
    def getDimension(self):
        return self.dimension
    
    def distanceTo(self, otherPoint):
        if self.dimension != otherPoint.getDimension():
            raise ValueError("Dimention has to be same")
        else:
            distance = 0
            for i in range(self.dimension):
                distance += (self.getCoords(i) - otherPoint.getCoords(i))**2
            return math.sqrt(distance)
