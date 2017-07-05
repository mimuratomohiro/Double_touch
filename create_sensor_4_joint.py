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

def sensor_result(points,sensor,hand_size):
	result = []
	for point in points:
		double_touch_point = np.zeros(sensor.size)
		for i in range(sensor.size):
			if(point + hand_size > sensor[i] and sensor[i] > point - hand_size ):
				double_touch_point[i] = 1
		result.append(double_touch_point)
	return np.array(result)

if __name__ == '__main__':
	points2    = np.sort(create_point(1,1,100))
	points3    = np.sort(create_point(1,1,100))
	points4    = np.sort(create_point(1,1,100))
	points5    = np.sort(create_point(1,1,100))
	
	hand_size  = 0.1
	#plot(points)
	Cube_2  = np.loadtxt("./Assets/data/Cube_2_on.csv",delimiter=",")
	Cube_3  = np.loadtxt("./Assets/data/Cube_3_on.csv",delimiter=",")
	Cube_4  = np.loadtxt("./Assets/data/Cube_4_on.csv",delimiter=",")
	Cube_5  = np.loadtxt("./Assets/data/Cube_5_on.csv",delimiter=",")

	Cube_2 = np.c_[Cube_2,np.ones(Cube_2.shape[0])*2]
	Cube_3 = np.c_[Cube_3,np.ones(Cube_3.shape[0])*3]
	Cube_4 = np.c_[Cube_4,np.ones(Cube_4.shape[0])*4]
	Cube_5 = np.c_[Cube_5,np.ones(Cube_5.shape[0])*5]
	Cube   = np.r_[Cube_2,Cube_3,Cube_4,Cube_5]

	Cube_2_point = Cube_2.T[0]
	Cube_3_point = Cube_3.T[0]
	Cube_4_point = Cube_4.T[0]
	Cube_5_point = Cube_5.T[0]


	result2 = sensor_result(Cube_2_point,points2,hand_size)
	result3 = sensor_result(Cube_3_point,points3,hand_size)
	result4 = sensor_result(Cube_4_point,points4,hand_size)
	result5 = sensor_result(Cube_5_point,points5,hand_size)

	time   = np.sort(np.unique(Cube.T[6]))

	ct2 = 0
	ct3 = 0
	ct4 = 0
	ct5 = 0 
	
	result       = []
	result_angle = []
	result_point = []
	result_move  = []
	
	for ti in time:
		in_vec = np.zeros(result2.shape[1]+result3.shape[1]+result4.shape[1]+result5.shape[1],dtype=np.bool)
		angle  = np.zeros(4)
		double = np.zeros(2)
		next_  = np.ones(4)
		move   = np.zeros(4)

		
		while next_.sum() != 0:

			if ct2 == Cube_2.shape[0]:
				next_[0] = 0
			elif(ti == Cube_2[ct2,6]):
				angle[0] =  Cube_2[ct2,1]
				angle[1] =  Cube_2[ct2,2]
				double[0] =  Cube_2[ct2,4]
				double[1] =  Cube_2[ct2,5]
				move[0]   =  1
				for j in range(result2.shape[1]):
					in_vec[j] += result2[ct2][j]
				if(ct2<=(Cube_2.shape[0]-1)):
					ct2 += 1
			else:
				next_[0] = 0

			if ct3 == Cube_3.shape[0]:
				next_[1] =0
			elif(ti == Cube_3[ct3,6]):
				angle[2] =  Cube_3[ct3,1]
				angle[3] =  Cube_3[ct3,2]
				double[0] =  Cube_3[ct3,4]
				double[1] =  Cube_3[ct3,5]
				move[1]   =  1
				for j in range(result3.shape[1]):
					in_vec[result2.shape[1]+j] += result3[ct3][j]
				if(ct3<=(Cube_3.shape[0]-1)):
					ct3 += 1
			else:
				next_[1] = 0

			if ct4 == Cube_4.shape[0]:
				next_[2] =0
			elif(ti == Cube_4[ct4,6]):
				angle[0] =  Cube_4[ct4,1]
				angle[1] =  Cube_4[ct4,2]
				double[0] =  Cube_4[ct4,4]
				double[1] =  Cube_4[ct4,5]
				move[2]   =  1
				for j in range(result4.shape[1]):
					in_vec[result2.shape[1]+result3.shape[1]+j] += result4[ct4][j]
				if(ct4<=(Cube_4.shape[0]-1)):
					ct4 += 1
			else:
				next_[2] = 0

			if ct5== Cube_5.shape[0]:
				next_[3] = 0
			elif(ti == Cube_5[ct5,6]):
				angle[2] =  Cube_5[ct5,1]
				angle[3] =  Cube_5[ct5,2]
				double[0] =  Cube_5[ct5,4]
				double[1] =  Cube_5[ct5,5]
				move[3]   =  1
				for j in range(result5.shape[1]):
					in_vec[result2.shape[1]+result3.shape[1]+result4.shape[1]+j] += result5[ct5][j]
				if(ct5 <=(Cube_5.shape[0]-1)):
					ct5 += 1
			else:
				next_[3] = 0
			
		result.append(in_vec)
		result_angle.append(angle)
		result_point.append(double)
		result_move.append(move)
	result       = np.array(result)
	result_angle = np.array(result_angle)
	result_point = np.array(result_point)
	result_move  = np.array(result_move)

	np.save("point2.npy",points2)
	np.save("point3.npy",points3)
	np.save("point4.npy",points4)
	np.save("point5.npy",points5)

	np.save("result.npy",result)
	np.save("result_angle.npy",result_angle)
	np.save("result_point.npy",result_point)
	np.save("result_angle_sin.npy",np.sin(result_angle))
	np.save("result_angle_cos.npy",np.cos(result_angle))
	np.save("result_move.npy",result_move)




	