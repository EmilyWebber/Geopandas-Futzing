import os
import fiona
from matplotlib import pyplot as plt


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

if __name__ == "__main__":
	input_file = "/Users/Emily/Desktop/SciPy-Tutorial-2015/examples/nybb_15b/nybb.shp"

	# print_a_few_lines(input_file)

	map_it(input_file)