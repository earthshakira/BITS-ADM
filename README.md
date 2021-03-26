# BITS-ADM

## lab_01 - FP Tree

Here, we try to create a FP Tree for cases similar to the market-basket analysis. 

[fp.py](https://github.com/earthshakira/BITS-ADM/blob/master/lab_01/fp.py) has code related to Preprocessing of data and construction of tree
The output of the fp tree is a **.dot** file that can be used to visualize the generated tree using **graphviz**.

## lab_02 - Decision Tree

We implemented the Decision Tree Creation algorithm using Information Gain. The code is given [here](https://github.com/earthshakira/BITS-ADM/blob/master/lab_02/decision-tree.py) and the generated tree can be seen [here.](https://github.com/earthshakira/BITS-ADM/blob/master/lab_02/Tree.pdf)

## lab_03 - Analysis of Discetization

Here we had to compare the performance of various discretization approaches like equal width binning and equal frequency binning on some standardized datasets and observe how various classification techniques are affected by it. The code is present at the [following link](https://github.com/earthshakira/BITS-ADM/blob/master/lab_03/Discretizers/discretization.py) and visualizations are present in [this folder](https://github.com/earthshakira/BITS-ADM/tree/master/lab_03/Discretizers), the file name is in following format `{discretizer}_{x_bins}_{y_bins}.png` . Most of it is taken from [this scikit ref](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization_classification.html#sphx-glr-auto-examples-preprocessing-plot-discretization-classification-py). The results are also compiled in the [results.csv](https://github.com/earthshakira/BITS-ADM/blob/master/lab_03/Findings%20Data%20Mining%20-%20results.csv) which gives additional information like _f1 score, precision and recall_.
