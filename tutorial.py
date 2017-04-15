import os
import fiona
from matplotlib import pyplot as plt
from shapely.geometry import Point, LineString, Polygon, MultiPoint, GeometryCollection
import rasterio
import cartopy.crs as ccrs
from rasterio.features import rasterize
from geopandas import read_file


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


def rasterio_exercise():
	utm18n = ccrs.UTM(18)
	ax = plt.axes(projection=utm18n)
	plt.title("UTM zone 18N")
	raster_file = "/Users/Emily/Desktop/SciPy-Tutorial-2015/data/manhattan.tif"
	with rasterio.open(raster_file) as src:
		left, bottom, right, top = src.bounds
		ax.imshow(src.read(1), origin="upper", extent=(left, right, bottom, top), cmap="gray")
		x = [left, right, right, left, left]
		y = [bottom, bottom, top, top, bottom]
		ax.coastlines(resolution="10m", linewidth=4, color="red")
		ax.gridlines(linewidth=2, color="lightblue", alpha=0.5, linestyle="--")
		plt.savefig("rasterio_cartopy.png", dpi=300)
		plt.show()

def show_img(img, bounds):
	left, bottom, right, top = bounds
	plt.imshow(img, cmap="gray", extent=(left, right, bottom, top))
	locs, labels = plt.xticks()
	plt.setp(labels, rotation=90)

def rasterio_mask():
	vector_file = "/Users/Emily/Desktop/SciPy-Tutorial-2015/examples/nybb_15b/nybb.shp"
	raster_file = "/Users/Emily/Desktop/SciPy-Tutorial-2015/data/manhattan.tif"
	df = read_file(vector_file)
	plt.figure(1)
	with rasterio.open(raster_file) as src:
		poly = df.to_crs(src.crs).ix[3]["geometry"]
		coords = [p.exterior.coords.xy for p in poly]
		ax = plt.subplot(1,2,1)
		img = src.read(1)
		show_img(src.read(1), src.bounds)
		for x, y in coords:
			plt.plot(x, y, color="red", linewidth=2)
		ax.set_xlim(src.bounds.left, src.bounds.right)
		ax.set_ylim(src.bounds.bottom, src.bounds.top)
		plt.subplot(1,2,2)
		mask = rasterize([poly], transform=src.transform, out_shape=src.shape)
		img[mask==0] = 225
		show_img(img, src.bounds)
	plt.savefig("rasterize_mask.png", dpi=300)
	plt.figure(2)
	show_img(mask, src.bounds)
	plt.savefig("mask.png", dpi=300)
	plt.show()

if __name__ == "__main__":
	input_file = "/Users/Emily/Desktop/SciPy-Tutorial-2015/examples/nybb_15b/nybb.shp"

	# print_a_few_lines(input_file)

	# map_it(input_file)

	# shapely_exercise()

	# rasterio_exercise()

	rasterio_mask()