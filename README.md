# Matilde's module to play Conway's game of life

Python implementation of Conway's game of life, as well as the functions to play it with and without the option of dynamically plotting the system.

## Using the code

The player simply has to, in his/her code, generate a grid of 0s and 1s and play the game. I recommend the plotting options for smaller grids (no more than 500x500 cells).

## Installing it
To install it, just type on your terminal:
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple gameoflife-matilde-module

The user must have numpy, matplotlib and IPython previously installed (the setup doesn't have a build dependencies option so the package "doesn't know" what the dependencies are to use the code).

For a dynamical installation (so that the package on the local machine is updated upon changes to the code), simply clone and pull the contents of the repository and pip install -e inside the folder "GameofLife".

## Contributing to the code
To contribute to the code, colaborators can create a secondary branch, change the code and do a pull request upon which the merge with the main branch will be approved/denied according to the status of the workflow "runtests", which preforms both unit and regression tests on the code after changes are executed. Only the owner can work on the main branch

