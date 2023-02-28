from Class.Point import Point
from Class.PointManager import PointManager
import time
import sys
from colorama import Fore, Back

dim = 0
n = 0
pm = PointManager()


def promptInput():
    inputFile = input(Fore.BLUE + "Apakah ingin membaca poin dari file? (Y/N)\n")
    if inputFile == "Y" or inputFile == "y":
        try:
            fileName = input("Input nama file (co: tes.txt): ")
            path = sys.path[0] + "\\Input\\" + fileName
            pm.readPoints(path)
        except:
            print("Invalid file")
            exit(0)
    else:
        dim = int(input("Insert the number of dimensions (dim) (>= 1): "))
        n = int(input("Insert the number of points (n): (>= 2): "))
        while n <= 1 or dim < 1:
            dim = int(input("Insert the number of dimensions (dim) (>= 1): "))
            n = int(input("Insert the number of points (n) (>= 2): "))
        pm.generateRandomPoints(n, dim)


def promptPlot():
    answer = ""
    flag = False
    while not flag:
        answer = input(Fore.BLUE + "Do you want to plot the points? Y/N\n")
        if answer == "Y" or answer == "y" or answer == "N" or answer == "n":
            flag = not flag

    if answer == "Y" or answer == "y":
        pm.plot()
    else:
        print("Program Exit")
        exit(0)


def main():
    promptInput()

    pm.mergeSort(pm.getPoints())

    dnc_start_time = time.time()
    dnc_shortestPairDistance = pm.divideAndConquerSolution()
    dnc_count = pm.getEuclideanDistanceCount()
    dnc_solPointOne = pm.getDNCSolPointOne()
    dnc_solPointTwo = pm.getDNCSolPointTwo()

    dnc_end_time = time.time()
    dnc_elapsed_time = dnc_end_time - dnc_start_time
    print(
        Fore.GREEN
        + "============================================================================================================================================"
    )

    print(
        f"[Divide and Conquer] Shortest Pair Distance is {dnc_shortestPairDistance:.2f} of point {dnc_solPointOne.printSelf()} and {dnc_solPointTwo.printSelf()}"
    )
    print(
        Fore.GREEN
        + f"[Divide and Conquer] Euclidean Distance Calculation Count (Divide and Conquer): {dnc_count}"
    )
    print(
        Fore.GREEN
        + f"[Divide and Conquer] Elapsed time: {dnc_elapsed_time:.6f} seconds"
    )

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
    bf_count = pm.getEuclideanDistanceCount()
    bf_elapsed_time = bf_end_time - bf_start_time
    print(
        Fore.RED
        + "============================================================================================================================================"
    )

    print(
        f"[Brute Force] Shortest Pair Distance is {bf_shortestPairDistance:.2f} of point {bf_solPointOne.printSelf()} and {bf_solPointTwo.printSelf()}"
    )
    print(f"[Brute Force] Euclidean Distance Calculation Count: {bf_count}")
    print(f"[Brute Force] Elapsed time: {bf_elapsed_time:.6f} seconds")

    print(
        "============================================================================================================================================"
    )

    answer_save = input("Want to save file? Y/N \n")
    if answer_save.lower() == "y":
        file_name = sys.path[0] + "/" + "Output/log_" + str(time.time())
        f = open(file_name, "w+")
        f.write(
            "============================================================================================================================================\n"
        )

        f.write(
            f"[Divide and Conquer] Shortest Pair Distance is {dnc_shortestPairDistance:.2f} of point {dnc_solPointOne.printSelf()} and {dnc_solPointTwo.printSelf()} \n"
        )
        f.write(
            f"[Divide and Conquer] Euclidean Distance Calculation Count (Divide and Conquer): {dnc_count} \n"
        )
        f.write("[Divide and Conquer] Elapsed time: {dnc_elapsed_time:.6f} seconds\n")

        f.write(
            "============================================================================================================================================\n"
        )
        f.write(
            "============================================================================================================================================\n"
        )
        f.write(
            f"[Brute Force] Shortest Pair Distance is {bf_shortestPairDistance:.2f} of point {bf_solPointOne.printSelf()} and {bf_solPointTwo.printSelf()}\n"
        )
        f.write(f"[Brute Force] Euclidean Distance Calculation Count: {bf_count}\n")
        f.write(f"[Brute Force] Elapsed time: {bf_elapsed_time:.6f} seconds\n")

        f.write(
            "============================================================================================================================================\n"
        )
        print("File saved at " + file_name)
        f.close()

    promptPlot()


if __name__ == "__main__":
    main()
