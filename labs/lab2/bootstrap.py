import matplotlib
matplotlib.use('Agg')

import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np 




def boostrap(statistic_func, iterations, data):
	samples  = np.random.choice(data,replace = True, size = [iterations, len(data)])
	#print samples.shape
	data_std = data.std()
	vals = []
	for sample in samples:
		sta = statistic_func(sample)
		#print sta
		vals.append(vals)
	b = np.array(vals)
	#print b
	lower, upper = np.percentile(b, [2.5, 97.5])
	return data_std,lower, upper



if __name__ == "__main__":
	df = pd.read_csv('./salaries.csv')
	#print df.columns
	
	data = df.values.T[0][0:79]
	data0 = df.values.T[1][0:79]
	
	boots = []
	boots0 = []
	

	boot = boostrap(np.std, 10000, data)



	boot0 = boostrap(np.std, 10000, data0)

	print boot
	print boot0

	