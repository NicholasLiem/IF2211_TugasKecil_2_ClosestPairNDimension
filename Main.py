from Class.Point import Point
from Class.PointManager import PointManager
import time

start_time = time.time()

# Luaran program:
# Sepasang titik yang jaraknya terdekat dan nilai jaraknya
# Banyak operasi perhitungan rumus Euclidean
# Waktu Riil dalam Detik
# Penggambaran grafik

# create some points
p1 = Point(1, 2, 3)
p2 = Point(4, 5, 6)
p3 = Point(7, 8, 9)

# create a PointManager and add the points to it
pm = PointManager()
pm.addPoint(p1)
pm.addPoint(p2)
pm.addPoint(p3)

# print(type(p1.coords))
# print(p1.getCoords(0))
# print(p1.getCoords(1))
# print(p1.getCoords(2))

# calculate the distance between the first two points
dist = pm.getDistance(p2, p3)
print(f"Distance between p1 and p2: {dist}")

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.6f} seconds")

pm.plot()