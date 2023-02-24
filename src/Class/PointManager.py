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

    def getPoints(self):
        return self.points

    def addPoint(self, newPoint: Point) -> None:
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
            for j in range(i + 1, len(self.points)):
                distance = self.getDistance(self.points[i], self.points[j])
                if distance < shortestDistance:
                    self.bf_solPointOne = self.points[i]
                    self.bf_solPointTwo = self.points[j]
                    shortestDistance = distance
        self.bf_solPointOne.setSolution()
        self.bf_solPointTwo.setSolution()
        return shortestDistance

    def divideAndConquerSolution(self) -> float:
        # TODO: Perlu diimplementasiin
        ...

    def splitPoints(self, point: Point):
        return self.points[:point], self.points[point:]

    def mergeSort(self, pointArray, coord : int):

        # Divide
        if len(pointArray) > 1:
            mid = len(pointArray)//2
            left = pointArray[:mid]
            right = pointArray[mid:]

            # Conquer
            self.mergeSort(left)
            self.mergeSort(right)

            i = j = k = 0 
            # Merge
            # Proses mengisi ulang pointArray
            while (i < len(left)) and (j < len(right)):
                if left[i].getCoords(coord) < right[j].getCoords(coord):
                    pointArray[k] = left[i]
                    i += 1
                else:
                    pointArray[k] = right[j]
                    j += 1
                k+= 1

            # Kasus array sisa
            while i < len(left):
                pointArray[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                pointArray[k] = right[j]
                j+= 1
                k+= 1

    def generateRandomPoints(self, n, dim):
        # TODO: Generate untuk n dimension
        for i in range(n):
            points = []
            for elem in range(dim):
                points.append(random.randint(0, 100))
            self.addPoint(Point(points))

    def plot(self) -> None:
        dim = self.points[0].getDimension()
        if self.points[0].getDimension() > 3:
            print("Sorry, dimension too high to visualize!")
        if dim == 3:
            self.plot3D()
        elif dim == 2:
            self.plot2D()
        elif dim == 1:
            self.plot1D()

    def plot3D(self) -> None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        for p in self.points:
            if p.getSolution():
                ax.scatter(
                    [p.getCoords(0)],
                    [p.getCoords(1)],
                    [p.getCoords(2)],
                    c="red",
                    marker="o",
                    s=90,
                )
            else:
                ax.scatter(
                    [p.getCoords(0)],
                    [p.getCoords(1)],
                    [p.getCoords(2)],
                    c="blue",
                    marker="o",
                    s=90,
                )
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.set_aspect("auto", adjustable="box")
        plt.show()

    def plot2D(self) -> None:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        for p in self.points:
            if p.getSolution():
                ax.scatter(
                    [p.getCoords(0)],
                    [p.getCoords(1)],
                    c="red",
                    marker="o",
                    s=90,
                )
            else:
                ax.scatter(
                    [p.getCoords(0)],
                    [p.getCoords(1)],
                    c="blue",
                    marker="o",
                    s=90,
                )
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_aspect("equal", adjustable="box")
        plt.show()

    def plot1D(self) -> None:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        for p in self.points:
            if p.getSolution():
                ax.scatter(
                    [p.getCoords(0)],
                    [0],
                    c="red",
                    marker="o",
                    s=90,
                )
            else:
                ax.scatter(
                    [p.getCoords(0)],
                    [0],
                    c="blue",
                    marker="o",
                    s=90,
                )
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        plt.show()
