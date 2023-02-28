from Class.Point import Point
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import math
import ast

class PointManager:
    def __init__(self):
        self.euclideanDistanceCount = 0
        self.bf_solPointOne = None
        self.bf_solPointTwo = None
        self.dnc_solPointOne = None
        self.dnc_solPointTwo = None
        self.points = []
        self.pivot = None
        self.distance = None

    def readPoints(self, path):
        self.points = []
        with open(path, "r") as f:
            lines = [line.strip("\n") for line in f]
            for line in lines:
                pointz = ast.literal_eval(line[7:])
                pointbaru = Point(pointz)
                self.points.append(pointbaru)

    def setPoints(self, array):
        self.points = array

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
        if len(self.points) == 1 or len(self.points) == 0:
            self.distance = float("inf")
            return
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
        self.distance = shortestDistance
        return shortestDistance

    def divideAndConquerSolution(self) -> float:
        if len(self.points) == 1:
            self.distance = float("inf")
            return
        elif len(self.points) == 2:
            self.distance = self.getDistance(self.points[0], self.points[1])
            self.dnc_solPointOne = self.points[0]
            self.dnc_solPointTwo = self.points[1]
            return
        leftPM, rightPM = self.splitPoints()
        leftPM.divideAndConquerSolution()
        rightPM.divideAndConquerSolution()
        self.conquer(leftPM, rightPM)
        return self.distance

    def conquer(self, leftPM, rightPM):
        # print("Conquer ", str(leftPM.points), str(rightPM.points))
        # print("\nLEFT & RIGHT SOL\n")
        # print(leftPM.dnc_solPointOne, leftPM.dnc_solPointTwo)
        # print(rightPM.dnc_solPointOne, rightPM.dnc_solPointTwo)
        # print("\n")
        leftDistance = leftPM.distance
        rightDistance = rightPM.distance
        # print("\n LEFT & RIGHT DIST\n")
        # print(str(leftDistance) + "---" + str(rightDistance))
        # print("\n")
        if leftDistance < rightDistance:
            self.distance = leftDistance
            self.dnc_solPointOne = leftPM.dnc_solPointOne
            self.dnc_solPointTwo = leftPM.dnc_solPointTwo
        else:
            self.distance = rightDistance
            self.dnc_solPointOne = rightPM.dnc_solPointOne
            self.dnc_solPointTwo = rightPM.dnc_solPointTwo

        minDist = min(leftDistance, rightDistance)
        pivot = self.pivot
        # print("Getting delta")
        pointsLeft = leftPM.getDelta(pivot, minDist)
        pointsRight = rightPM.getDelta(pivot, minDist)
        distance, sol1, sol2 = self.compare(pointsLeft, pointsRight, minDist)

        self.euclideanDistanceCount += (
            leftPM.euclideanDistanceCount + rightPM.euclideanDistanceCount
        )

        if distance < minDist:
            self.distance = distance
            self.dnc_solPointOne = sol1
            self.dnc_solPointTwo = sol2
        # print("\nRESULT ")
        # print(self.distance)
        # print(self.dnc_solPointOne, self.dnc_solPointTwo)

    def compare(self, pointsLeft, pointsRight, minDist):
        distance = float("inf")
        sol1 = None
        sol2 = None
        for pointL in pointsLeft:
            for pointR in pointsRight:
                if not pointL.scanNear(pointR, minDist):
                    continue
                dist = self.getDistance(pointL, pointR)
                if dist < distance:
                    distance = dist
                    sol1 = pointL
                    sol2 = pointR
        return distance, sol1, sol2

    def getDelta(self, pivot, minDist):
        points = []
        for point in self.points:
            if point.nearPivot(pivot, minDist):
                points.append(point)
        return points

    def splitPoints(self):
        midPoint = math.floor(len(self.points) / 2)
        left = PointManager()
        left.setPoints(self.points[:midPoint])
        right = PointManager()
        right.setPoints(self.points[midPoint:])
        self.pivot = self.points[midPoint - 1].average(self.points[midPoint])
        return left, right
    
    def mergeSort(self, pointArray):
        # Divide
        if len(pointArray) > 1:
            mid = len(pointArray) // 2
            left = pointArray[:mid]
            right = pointArray[mid:]

            # Conquer
            self.mergeSort(left)
            self.mergeSort(right)

            i = j = k = 0
            # Merge
            # Proses mengisi ulang pointArray
            while (i < len(left)) and (j < len(right)):
                if left[i].lessThan(right[j]):
                    pointArray[k] = left[i]
                    i += 1
                else:
                    pointArray[k] = right[j]
                    j += 1
                k += 1

            # Kasus array sisa
            while i < len(left):
                pointArray[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                pointArray[k] = right[j]
                j += 1
                k += 1

    def generateRandomPoints(self, n, dim):
        # TODO: Generate untuk n dimension
        for i in range(n):
            points = []
            for elem in range(dim):
                points.append(random.uniform(-1e9, 1e9))
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
