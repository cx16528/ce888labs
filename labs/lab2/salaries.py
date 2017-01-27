import matplotlib
matplotlib.use('Agg')

import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np 




# def permutation(statistic, error):


def mad(arr):
    """ Median Absolute Deviation: a "Robust" version of standard deviation.
        Indices variabililty of the sample.
        https://en.wikipedia.org/wiki/Median_absolute_deviation 
        http://stackoverflow.com/questions/8930370/where-can-i-find-mad-mean-absolute-deviation-in-scipy
    """
    arr = np.ma.array(arr).compressed() # should be faster to not use masked arrays.
    med = np.median(arr)
    return np.median(np.abs(arr - med))


if __name__ == "__main__":
	#df = pd.read_csv('./customers.csv') 
	df = pd.read_csv('./vehicles.csv')
	print df.columns
	print df.columns[1]
	sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)

	sns_plot.axes[0,0].set_ylim(0,)
	sns_plot.axes[0,0].set_xlim(0,)

	sns_plot.savefig("scaterplot.png",bbox_inches='tight')
	sns_plot.savefig("scaterplot.pdf",bbox_inches='tight')
	
	#print df.values.T[1]
	data1 = df.values.T[1][0:79]
	data0 = df.values.T[0][0:79]
	
	print ("Current Fleet Mean: %f")%(np.mean(data0))
	print ("Current Fleet Median: %f")%(np.median(data0))
	print ("Current Fleet Var: %f")%(np.var(data0))
	print ("Current Fleet std: %f")%(np.std(data0))
	print ("Current Fleet MAD: %f")%(mad(data0))

	print ("New Fleet Mean: %f")%(np.mean(data1))
	print ("New Fleet Median: %f")%(np.median(data1))
	print ("New Fleet Var: %f")%(np.var(data1))
	print ("New Fleet std: %f")%(np.std(data1))
	print ("New Fleet MAD: %f")%(mad(data1))

	plt.clf()
	sns_plot2 = sns.distplot(data0,bins = 20, kde=False, rug=True).get_figure()

	axes = plt.gca()
	axes.set_xlabel('Current Fleet') 
	axes.set_ylabel('Current Fleet count')

	sns_plot2.savefig("histogram_current_fleet.png",bbox_inches='tight')
	sns_plot2.savefig("histogram_current_fleet.pdf",bbox_inches='tight')

	plt.clf()
	sns_plot3 = sns.distplot(data1,bins = 20, kde=False, rug=True).get_figure()

	axes = plt.gca()
	axes.set_xlabel('Proposed Fleet') 
	axes.set_ylabel('Proposed Fleet count')

	sns_plot3.savefig("histogram_new_fleet.png",bbox_inches='tight')
	sns_plot3.savefig("histogram_new_fleet.pdf",bbox_inches='tight')

	