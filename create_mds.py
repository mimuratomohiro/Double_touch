# coding: UTF-8

import numpy as np
import scipy as sp
import scipy.stats as ss
import csv
from time import time

class chnge_MDS():
	def __init__(self,data,N):
		self.data   = data
		self.N      = N
		self.point  = np.random.rand(data.shape[0])*10

	def create_map(self):
		for i in range(self.N):
			self.update(self.data)

	def update(self, data ):
		fi    = np.zeros(self.point.shape[0])

		for row , i in zip(data , range(self.point.shape[0])):
			for dist , j in zip(row,range(self.point.shape[0])):
				if dist != 1:
					fi[i] += (abs(self.point[i]-self.point[j])-dist)*(self.point[j]-self.point[i])/abs(self.point[j]-self.point[i])
			self.point[i] = self.point[i] + (fi[i] / self.point.shape[0])
		print(abs(fi).sum())

		

if __name__ == '__main__':
	distance1 = np.load("distance1.npy")
	distance2 = np.load("distance2.npy")
	point1    = np.load("point1.npy")
	point2    = np.load("point2.npy")

	
	creata_map = chnge_MDS(distance1,400)
	creata_map.create_map()



