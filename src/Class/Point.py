import math


class Point:

    # coords adalah tuple yang isinya value koordinatnya
    # dimension adalah berapa jumlah dimensinya

    def __init__(self, *args):
        self.coords = args[0]
        self.dimension = len(self.coords)
        self.solution = False

    def setSolution(self):
        self.solution = True

    def getSolution(self):
        return self.solution

    def printSelf(self):
        return f"Point: {self.coords}"

    def getCoords(self, index) -> float:
        return self.coords[index]

    def getDimension(self) -> int:
        return self.dimension

    def distanceTo(self, otherPoint) -> float:
        if self.dimension != otherPoint.getDimension():
            raise ValueError("Dimension has to be same")
        else:
            distance = 0
            for i in range(self.dimension):
                distance += (self.getCoords(i) - otherPoint.getCoords(i)) ** 2
            return math.sqrt(distance)

    def lessThan(self, otherPoint) -> bool:
        ax_ind = 0
        while ax_ind < self.dimension and self.getCoords(
            ax_ind
        ) == otherPoint.getCoords(ax_ind):
            ax_ind += 1
        if self.getCoords(ax_ind) < otherPoint.getCoords(ax_ind):
            return True
        else:
            return False
