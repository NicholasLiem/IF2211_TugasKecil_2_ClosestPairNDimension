from Class.Point import Point
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class PointManager:

    def __init__(self):
        self.points = []

    def addPoint(self, newPoint : Point):
        self.points.append(newPoint)
        
    def removePoint(self, point: Point):
        self.points.remove(point)

    def getDistance(self, pointOne: Point, pointTwo: Point):
        return pointOne.distanceTo(pointTwo)

    # def splitPoints(self, point: Point):
    #     return self.points[:point], self.points[point:]
    
    # def quickSort(self, left, right):
        
    
    # def partition(self, left, right):
        

    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for p in self.points:
            ax.scatter([p.getCoords(0)], [p.getCoords(1)], [p.getCoords(2)], c='r', marker='o')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()
    