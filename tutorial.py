import os
import fiona
from matplotlib import pyplot as plt
from shapely.geometry import Point, LineString, Polygon, MultiPoint, GeometryCollection


def print_a_few_lines(input_file):
	with fiona.open(input_file) as src:
		f = src.next()
		print (f["geometry"]["type"])
		print (f["properties"])

def map_it(input_file):
	plt.figure(figsize=(6,6))
	with fiona.open(input_file) as src:
		f = src.next()
		for coords in f["geometry"]["coordinates"]:
			x, y = zip(*coords[0])
			plt.plot(x, y)
		plt.gca().set_aspect("equal")
		plt.show()


def shapely_exercise():
	l1 = [0, 1, 2, 0, 1, 2]
	l2 = [0, 0, 0, 1, 1, 1]
	pts = [Point(x, y) for x, y in zip(l1, l2)]
	MultiPoint(pts)

if __name__ == "__main__":
	input_file = "/Users/Emily/Desktop/SciPy-Tutorial-2015/examples/nybb_15b/nybb.shp"

	# print_a_few_lines(input_file)

	# map_it(input_file)

	# shapely_exercise()
	l1 = [0, 1, 2, 0, 1, 2]
	l2 = [0, 0, 0, 1, 1, 1]
	pts = [Point(x, y) for x, y in zip(l1, l2)]
	MultiPoint(pts)