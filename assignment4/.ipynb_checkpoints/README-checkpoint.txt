# Georgia Tech OMSCS - CS7641 - Machine Learning Assignment 4 Code

I used a conda environment to run the code. After activating a conda environment, make sure to install Scikit-learn, Tensorflow, Keras, Jupyter with Python version 3.x., and the hiive mdptoolbox.

Forest management experiments can just be re-run as it didn't take much time. Frozen lake experiment results can loaded from relevant CSVs in the frozen_lake/output directory

conda install dill

in your conda environment.

Step-by-step:

1. Clone this repository[https://github.com/eugeneoh/CS7641.git] and then cd into the directory
2. cd into the assignment4 directory
3. conda create -n cs7641
4. conda activate cs7641
5. conda install -c conda-forge tensorflow
6. conda install dill
7. git clone https://github.com/hiive/hiivemdptoolbox.git
8. cd hiivemdptoolbox
9. pip install -e .


To run forest management experiments 
1. cd into the assignment4 directory after running the above steps
2. jupyter-lab

To run the frozen lake experiments
1. cd frozen_lake
2. python run_experiment.py --all --plot