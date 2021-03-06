# Lab6



## Lab Exercises 

- [ ] Use a seaborn pairplot ``sns.pairplot()'' to visualise your data
- ![scatterplot](./pairplot.png?raw=true)
- [ ] Loop over different cluster size starting from 2 until 10, using all the features present and pick the one with the lowest silhouette score
- Number of clusters: 3
- Silhouette Coefficient: 0.170
- [ ] (Optional) Save 10 runs for each cluster size and use a seaborn pointplot [http://seaborn.pydata.org/generated/seaborn.pointplot.html](http://seaborn.pydata.org/generated/seaborn.pointplot.html) without joining the lines 
to plot the confidence intervals for the silhouette score
- ![scatterplot](./Kmeans_cluster.png?raw=true)
- [ ] Change your clusterer to ``AgglomerativeClustering'' see here for more [http://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html) and re-do the above experiment - what do you observe?
- ![scatterplot](./AgglomerativeClustering.png?raw=true)

