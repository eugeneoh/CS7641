# Georgia Tech OMSCS - CS7641 - Machine Learning Assignment 3 Code

I used a conda environment to run the code. After activating a conda environment, make sure to install Scikit-learn, Tensorflow, Keras, Jupyter with Python version 3.x., and MLRose Hiive

All of the data is stored in this repository in the data folder. Relevant results are also stored in the results folder so if you don't want to run the code yourself you can use joblib.load to get the results of the experiment runs.
If you encounter an issue with a missing module named dill when loading these pkl files make sure to run:

conda install dill

in your conda environment.

Step-by-step:

1. Clone this repository[https://github.com/eugeneoh/CS7641.git] and then cd into the directory
2. cd into the assignment3 directory
3. conda create -n cs7641
4. conda activate cs7641
5. conda install -c conda-forge tensorflow
6. conda install dill
7. jupyter-lab
