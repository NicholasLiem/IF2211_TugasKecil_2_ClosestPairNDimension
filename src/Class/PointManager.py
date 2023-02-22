from Class.Point import Point
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
class PointManager:

    def __init__(self):
        self.euclideanDistanceCount = 0
        self.solPointOne = None
        self.solPointTwo = None
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

    def getSolPointOne(self) -> Point:
        return self.solPointOne
    
    def getSolPointTwo(self) -> Point:
        return self.solPointTwo

    def bruteForceSolution(self) -> float:
        shortestDistance = float("inf")
        for i in range(len(self.points)):
            for j in range(i+1, len(self.points)):
                distance = self.getDistance(self.points[i], self.points[j])
                if distance < shortestDistance:
                    self.solPointOne = self.points[i]
                    self.solPointTwo = self.points[j]
                    shortestDistance = distance
        return shortestDistance

    # def splitPoints(self, point: Point):
    #     return self.points[:point], self.points[point:]
    
    # def quickSort(self, left, right):
        
    # def partition(self, left, right):

    def generateRandomPoints(self, n):
        # Generate untuk n dimension
        for i in range(n):
            self.addPoint(Point(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)))

    def plot3D(self) -> None:
        # cek kalau bukan 3 dimensi ga bisa di plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for p in self.points:
            ax.scatter([p.getCoords(0)], [p.getCoords(1)], [p.getCoords(2)], c=random.randint(0, 100), marker='o', s=90)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()
    