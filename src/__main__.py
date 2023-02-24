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


def main():
    pm = PointManager()
    dim = int(input("Masukkan jumlah dimensi: "))
    n = int(input("Masukkan jumlah n: "))

    pm.generateRandomPoints(n, dim)
    pm.mergeSort(pm.getPoints())
    ## Ini test case yang salah
    pm.readPoints("tes.txt")
    pm.listPoints()

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
    print(f"[Brute Force] Elapsed time: {bf_elapsed_time:.6f} seconds")

    print(
        "============================================================================================================================================"
    )
    # reset Euclidean Count
    pm.resetEuclideanCount()

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

    # # Ini buat plotting 3D
    # pm.plot()


if __name__ == "__main__":
    main()
