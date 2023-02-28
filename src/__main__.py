from Class.Point import Point
from Class.PointManager import PointManager
import time
import sys

def main():
    pm = PointManager()
    inputFile = input("Apakah ingin membaca poin dari file? (Y/N)\n")
    if(inputFile == "Y" or inputFile == "y"):
        fileName = input("Input nama file (co: tes.txt): ")
        path = sys.path[0] + "\\Input\\" + fileName
        pm.readPoints(path)
    else:
        dim = int(input("Insert the number of dimensions (dim): "))
        n = int(input("Insert the number of points (n): "))
        while(n < 1 or dim < 1):
            dim = int(input("Insert the number of dimensions (dim): "))
            n = int(input("Insert the number of points (n): "))
        pm.generateRandomPoints(n, dim)

    pm.mergeSort(pm.getPoints())

    dnc_start_time = time.time()
    dnc_shortestPairDistance = pm.divideAndConquerSolution()
    dnc_solPointOne = pm.getDNCSolPointOne()
    dnc_solPointTwo = pm.getDNCSolPointTwo()

    dnc_end_time = time.time()
    dnc_elapsed_time = dnc_end_time - dnc_start_time
    print(
        "============================================================================================================================================"
    )

    print(
        f"[Divide and Conquer] Shortest Pair Distance is {dnc_shortestPairDistance:.2f} of point {dnc_solPointOne.printSelf()} and {dnc_solPointTwo.printSelf()}"
    )
    print(
        f"[Divide and Conquer] Euclidean Distance Calculation Count (Divide and Conquer): {pm.getEuclideanDistanceCount()}"
    )
    print(f"[Divide and Conquer] Elapsed time: {dnc_elapsed_time:.6f} seconds")

    print(
        "============================================================================================================================================"
    )
    # reset Euclidean Count
    pm.resetEuclideanCount()

    bf_start_time = time.time()
    bf_shortestPairDistance = pm.bruteForceSolution()
    bf_solPointOne = pm.getBFSolPointOne()
    bf_solPointTwo = pm.getBFSolPointTwo()
    bf_end_time = time.time()
    bf_elapsed_time = bf_end_time - bf_start_time
    print(
        "============================================================================================================================================"
    )

    print(
        f"[Brute Force] Shortest Pair Distance is {bf_shortestPairDistance:.2f} of point {bf_solPointOne.printSelf()} and {bf_solPointTwo.printSelf()}"
    )
    print(
        f"[Brute Force] Euclidean Distance Calculation Count: {pm.getEuclideanDistanceCount()}"
    )
    print(
        f"[Brute Force] Elapsed time: {bf_elapsed_time:.6f} seconds")

    print(
        "============================================================================================================================================"
    )
    time.sleep(2)

    answer = ''
    flag = False
    while(not flag):
        answer = input("Do you want to plot the points? Y/N\n")
        if (answer == "Y" or answer == "y" or answer == "N" or answer == "n"):
            flag = not flag
        
    if (answer == "Y" or answer == "y"):
        pm.plot()
    else:
        print("Program Exit")
        exit(0)

if __name__ == "__main__":
    main()
