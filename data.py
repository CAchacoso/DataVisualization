"""
Visualizing Data Points in High Dimensional Space
"""

import os
import csv
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

with open('spiral.csv') as csvfile:
	readCSV = csv.reader(csvfile)
	fig = plt.figure()
	ax = plt.axes(projection='3d')
	plt.title("Spiral.json Data Points")
	zline = np.linspace(0, 15, 1000)
	xline = np.cos(zline)
	yline = np.sin(zline)
	ax.scatter3D(xline, yline, zline, 'blue')

	# plt.zlabel('z-axis')
	# plt.alabel('a-axis')
	# plt.blabel('b-axis')
	# plt.clabel('c-axis')
	# plt.dlabel('d-axis')
	# plt.elabel('e-axis')
	# plt.flabel('f-axis')
	# plt.glabel('g-axis')
	# plt.hlabel('h-axis')
	# plt.ilabel('i-axis')
	# plt.jlabel('j-axis')
	# plt.klabel('k-axis')
	# plt.llabel('l-axis')
	# plt.mlabel('m-axis')
	# plt.nlabel('n-axis')
	# plt.olabel('o-axis')
	# plt.plabel('p-axis')
	# plt.qlabel('q-axis')

	# for col in readCSV:
	# 	point = col[0]
	# 	x = col[1]
	# 	y = col[2]
	# 	z = col[3]
	# 	ax.scatter3D(x, y, z, c=z)
		# a = col[4]
		# b = col[5]
		# c = col[6]
		# d = col[7]
		# e = col[8]
		# f = col[9]
		# g = col[10]
		# h = col[11]
		# i = col[12]
		# j = col[13]
		# k = col[14]
		# l = col[15]
		# m = col[16]
		# n = col[17]
		# o = col[18]
		# p = col[19]
		# q = col[20]
		# point = [x, y, z]
		# [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q]
		# print(point)

		# for row in col[0]:
		# 	plt.plot(data)

	plt.show()

