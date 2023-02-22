from Class.Point import Point
from Class.PointManager import PointManager
import time

    # Input program:
    # n
    # titik yang dibangkitkan secara acak dalam koordinat (x, y, z)

    # Luaran program:
    # Sepasang titik yang jaraknya terdekat dan nilai jaraknya
    # Banyak operasi perhitungan rumus Euclidean
    # Waktu Riil dalam Detik
    # Penggambaran grafik

def main ():
    pm = PointManager()
    n = int(input("Masukkan jumlah n: "))
    start_time = time.time()
    pm.generateRandomPoints(n)

    # create some points
    # p1 = Point(1, 2, 3, 999)
    # p2 = Point(4, 5, 6, 999)
    # p3 = Point(7, 8, 9, 7)

    # create a PointManager and add the points to it
    # pm.addPoint(p1)
    # pm.addPoint(p2)
    # pm.addPoint(p3)

    # print(type(p1.coords))
    # print(p1.getCoords(0))
    # print(p1.getCoords(1))
    # print(p1.getCoords(2))

    shortestPairDistanceBruteForce = pm.bruteForceSolution()
    solPointOne = pm.getSolPointOne()
    solPointTwo = pm.getSolPointTwo()
    print(f"Shortest Pair Distance (Brute Force) is {shortestPairDistanceBruteForce:.2f} of point {solPointOne.printSelf()} and {solPointTwo.printSelf()}")
    print("Euclidean Distance Calculation Count (Brute Force):", pm.getEuclideanDistanceCount())

    # Time Stuff
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.6f} seconds")

    # Ini buat plotting 3D
    pm.plot3D()
    
if __name__ == '__main__':
    main()