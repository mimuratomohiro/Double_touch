# coding: UTF-8

import numpy as np
import scipy as sp
import scipy.stats as ss
import csv
from time import time


if __name__ == '__main__':
	distance1 = np.load("distance1.npy")
	distance2 = np.load("distance2.npy")

	point1    = np.random.rand(distance1.shape[0])*distance1.max()
	point2    = np.random.rand(distance2.shape[0])*distance2.max()

	