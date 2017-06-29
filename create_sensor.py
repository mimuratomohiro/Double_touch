# coding: UTF-8

import numpy as np
import scipy as sp
import scipy.stats as ss
import matplotlib.pyplot as plt
import csv
from time import time

from matplotlib import offsetbox
from sklearn import (manifold, datasets, decomposition, ensemble,
                     discriminant_analysis, random_projection)


def create_point(alpha1,alpha2,number):
	point  = np.sort(np.random.beta(alpha1, alpha2, number))*4
	return point

def plot(point):
	plt.plot(point,np.ones(point.size),'o')
	plt.show()

def plot2(point):
	plt.plot(point,'o')
	plt.show()


if __name__ == '__main__':
	points1    = create_point(2,1,300)
	points2    = create_point(2,1,300)
	hand_size  = 0.3
	#plot(points)
	Cube_2_off = np.loadtxt("./Assets/data/Cube_2_off.csv",delimiter=",")
	Cube_2_on  = np.loadtxt("./Assets/data/Cube_2_on.csv",delimiter=",")
	Cube_3_off = np.loadtxt("./Assets/data/Cube_3_off.csv",delimiter=",")
	Cube_3_on  = np.loadtxt("./Assets/data/Cube_3_on.csv",delimiter=",")

	Cube_2_point = Cube_2_on.T[0]
	Cube_3_point = Cube_3_on.T[0]

	point_list1 = []
	point_list2 = []
	distance1   = np.ones((points1.size,points1.size))
	distance2   = np.ones((points2.size,points2.size))

	for point1, point2 in zip(Cube_2_point,Cube_3_point):
		double_touch_point1 = np.zeros(points1.size)
		double_touch_point2 = np.zeros(points2.size)

		for i in range(points1.size):
			if(point1 + hand_size > points1[i] and points1[i] > point1 - hand_size ):
				double_touch_point1[i] = 1

			if(point2 + hand_size > points2[i] and points2[i] > point2 - hand_size ):
				double_touch_point2[i] = 1

		for i in range(points1.size):
			if double_touch_point1[i] == 1:
				for j in range(i+1,points1.size):
					if double_touch_point1[j] == 1:
						distance1[i][j] += 1
						distance1[j][i] += 1

			if double_touch_point2[i] == 1:
				for j in range(i+1,points2.size):
					if double_touch_point2[j] == 1:
						distance2[j][i] += 1
						distance2[i][j] += 1


		point_list1.append(double_touch_point1)
		point_list2.append(double_touch_point2)

	with open("distance1.csv",'w') as f1:
		writer = csv.writer(f1, delimiter = ',')
		for row in distance1:
			writer.writerow(1./row)
	f1.close()

	with open("distance2.csv",'w') as f1:
		writer = csv.writer(f1, delimiter = ',')
		for row in distance2:
			writer.writerow(1./row)
	f1.close()
	np.save("distance1.npy", 1./distance1)
	np.save("distance2.npy", 1./distance2)
	np.save("point1.npy",points1)
	np.save("point2.npy",points2)

	#clf = manifold.MDS(n_components=1, n_init=1, max_iter=100)

	#X_mds = clf.fit_transform(1./distance1)
	#X_mds = ((X_mds - X_mds.min() )/(X_mds.max()- X_mds.min() ) )*4
	#plot(X_mds)


	#for i,j in zip( points,X_mds[:,0]):
#		print(i,j)
	



