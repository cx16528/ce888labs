# Lab5

#

## Lab Exercises 

- [ ] Load the data from the file ``jester-data-1.csv''
	* The data is from [http://eigentaste.berkeley.edu/dataset/](http://eigentaste.berkeley.edu/dataset/) and it contains the ratings of 101 jokes from 24,983 users
	* You can find the jokes in the website [http://eigentaste.berkeley.edu/dataset/jester_dataset_1_joke_texts.zip](http://eigentaste.berkeley.edu/dataset/jester_dataset_1_joke_texts.zip)

- [ ] Split the data into validation, test and training set with 80:10:10 proportions
 -[] Use numpy split function to divide data to tree parties.
- [ ] Use latent factor modelling to infer the hidden ratings of the users (they are labelled as "99" in the dataset) on the training set
 -[] It is working well.
- [ ] Calculate the performance of the algorithm in the validation dataset by looping through the dataset without training
- [ ] Change hyper-parameters (i.e. learning rates, number of iterations etc) as needed so you can get good results
- [ ] Report the MSE on the test dataset

- [ ] (if you have time) Use pandas to find the best and the worst rated jokes


