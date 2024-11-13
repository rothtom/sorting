# What is it?  

This project visualizes various sorting algorithms.

# All possible algorithms:  

- bogo-sort
- selection-sort
- bubble-sort
- merge-sort
- quick-sort
  
# Why did i create this project?  

This is a project I created for school.  

# Getting started:  

1. Download the github repo.
2. cd into the project directory
3. cd into the python directory
4. make sure you have a python interpreter installed
5. create a virtual environment for the packages we are going to install by running "python -m venv .venv"
 this creates a new foulder named ".venv" in the current directory. This i our virtual environment.
6. activate that venv by running source .venv/bin/activate
7. update the python package manager "pip" by running "pip install --upgrade pip"
8. install all required packages py running "pip install -r requirements.txt"

# Usage:  

python main.py  -a or --algorithm (any of the ones listed above and exactly spelled as above, you can leave out the "-sort".)

### optional parameters:  

- l or length: sets the length of the list you want to sort  
- d : sets delay after each drawing point in the visualisation  
- s or seed: sets the seed used for random shuffeling of the List in the beginning and bogo-sort.
- startin-tuple: a set of integers separated by only commas that is used as the list for sorting.


