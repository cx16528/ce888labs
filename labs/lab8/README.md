# Lab8



## Lab Exercises 

- [ ] run ``python imdb.py`` and note somewhere the test accuracy score 
- [ ]It is too slow
- [ ] Modify the code to add one more layer of 64 ``relu`` units after the embedding layer record the score (i.e. add a dense followed by an "activation" layer)
- [ ]Finished. This is similar with last labs.
- [ ] Modify the code and add a dropout layer after the relu layer
- [ ]Finished.
- [ ] Remove the layers you have added previously Convolution layer followed by a relu non-linearity and global max pooling (see lecture notes)
- [ ]Finished.
- [ ] Modify the code and add an LSTM layer in place of the convolution layer
- [ ]Finished. Finding that the LSRM layer and Convolution layer cannot put together derectly.
- [ ] (Optional - and quite advanced) use both an LSTM layer and a Convolution layer and merge the results with a Merge layer
- [ ]Finished. Using the merge of keras to contact LSTM model and Convolution model together and creating a final model with both of them function. Because of it spending a long time I did not get the final scores.
