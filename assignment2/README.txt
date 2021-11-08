# Georgia Tech OMSCS - CS7641 - Machine Learning Assignment 2 Code

I used a conda environment to run the code. After activating a conda environment, make sure to install Scikit-learn, Tensorflow, Keras, Jupyter with Python version 3.x., and MLRose Hiive

All of the data is stored in this repository in the data folder. Additionally, load the grid search results for the ANNs from the saved_ann_results directory to avoid taking the time to run your own search. Same for some of the longer runs such as the adult k-NN results and the adult SVM results.
If you encounter an issue with a missing module named dill when loading these pkl files make sure to run:

conda install dill

in your conda environment.

Step-by-step:

1. Clone this repository[https://github.com/eugeneoh/CS7641.git] and then cd into the directory
2. cd into the assignment2 directory
3. conda create -n cs7641
4. conda activate cs7641
5. conda install -c conda-forge tensorflow
6. conda install dill
7. pip install mlrose-hiive
8. jupyter-lab
