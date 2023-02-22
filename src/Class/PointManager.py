from Class.Point import Point
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
class PointManager:

    def __init__(self):
        self.euclideanDistanceCount = 0
        self.bf_solPointOne = None
        self.bf_solPointTwo = None
        self.dnc_solPointOne = None
        self.dnc_solPointTwo = None
        self.points = []

    def addPoint(self, newPoint : Point) -> None:
        self.points.append(newPoint)
        
    def removePoint(self, point: Point) -> None:
        self.points.remove(point)

    def listPoints(self) -> None:
        print("List of Points: ")
        for p in self.points:
            print(p.printSelf())

    def getEuclideanDistanceCount(self) -> int:
        return self.euclideanDistanceCount

    def getDistance(self, pointOne: Point, pointTwo: Point) -> float:
        self.euclideanDistanceCount += 1
        return pointOne.distanceTo(pointTwo)

    def getBFSolPointOne(self) -> Point:
        return self.bf_solPointOne
    
    def getBFSolPointTwo(self) -> Point:
        return self.bf_solPointTwo

    def getDNCSolPointOne(self) -> Point:
        return self.dnc_solPointOne

    def getDNCSolPointTwo(self) -> Point:
        return self.dnc_solPointTwo

    def resetEuclideanCount(self) -> None:
        self.euclideanDistanceCount = 0

    def bruteForceSolution(self) -> float:
        shortestDistance = float("inf")
        for i in range(len(self.points)):
            for j in range(i+1, len(self.points)):
                distance = self.getDistance(self.points[i], self.points[j])
                if distance < shortestDistance:
                    self.bf_solPointOne = self.points[i]
                    self.bf_solPointTwo = self.points[j]
                    shortestDistance = distance
        return shortestDistance

    def divideAndConquerSolution(self) -> float:
        # TODO: Perlu diimplementasiin
        ...

    def splitPoints(self, point: Point):
        return self.points[:point], self.points[point:]
    
    def quickSort(self, left, right):
        # TODO: Perlu diimplementasiin
        ...
        
    def partition(self, left, right):
        # TODO: Perlu diimplementasiin
        ...

    def generateRandomPoints(self, n):
        # TODO: Generate untuk n dimension
        for i in range(n):
            self.addPoint(Point(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)))

    def plot3D(self) -> None:
        # TODO: Cek kalau bukan 3 dimensi ga bisa di plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for p in self.points:
            ax.scatter([p.getCoords(0)], [p.getCoords(1)], [p.getCoords(2)], c=random.randint(0, 100), marker='o', s=90)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()
    