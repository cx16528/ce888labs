# Lab2

## Overleaf

Go to [www.overleaf.com](https://www.overleaf.com) and create an account and a new document.

## Setting up 
* Do the following from the unix prompt of your VM
	* Go to the directory you "cloned" the module files last time
	* Do `git pull origin master' to bring the new files

* Do the following tasks using your windows share or your unix account in the VM	
	* Copy the lab files from the module directory into your own github lab directory, in "lab2" folder
	* Remove everything from the copied README.md

## Histogram and Scatterplot

1. Read the data for the vehicles found in the file `vehicles.csv`
2. Create histograms and scatterplots for "current fleet" and "proposed fleet" - see `salaries.py` on how to do this

![scatterplot](./scaterplot.png?raw=true)
![histogram](./histogram_current_fleet.png?raw=true)
![histogram](./histogram_new_fleet.png?raw=true)

## Standard deviation comparison via the boostrap

- Find the standard deviation of both samples

Standard deviation of current  fleet is :4.170343
Standard deviation of proposed fleet is :6.068931

However the standard deviation of current fleet is better than standard deviation of proposed fleet

Use the example code for the bootstrap provided in ``bootstrap.py'' to do the following
- Find the upper and lower bound of the standard deviation of the current fleet
- Do the same with the new fleet

Lower of standard deviation of current  fleet is :3.3793
Lower of standard deviation of proposed  fleet is :5.1363
Upper of standard deviation of current  fleet is :4.8501
Upper of standard deviation of proposed  fleet is :6.9062


