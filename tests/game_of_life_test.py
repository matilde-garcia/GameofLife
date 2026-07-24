import pytest
import numpy as np
import os
import gameoflife_matilde_module


"""
We want to implement a unit test and a regression test. Therefore, we will test if 
some function is doing what it is supposed to be doing (unit testing). Then, we will 
also test if some change in the code changed the way the code should work.
"""

#-------------------------------------------------------UNIT TESING-------------------------------------------------------

generator = np.random.default_rng(0)
my_grid = (generator.random((50, 50)) < 0.30).astype(int)

#pretty lame test, but let's make sure it returns a grid with the same size
def test_lifegame():
    assert np.shape(gameoflife_matilde_module.life_game(my_grid)) == np.shape(my_grid)

#make sure a grid of only zeros returns a grid of only zeros
def test_lifegame2():
    assert np.array_equal(gameoflife_matilde_module.life_game(np.zeros(shape=(500,500))), np.zeros(shape=(500,500))) == True

#------------------------------------------------------REGRESSION TESTING----------------------------------------------------

#grid generated for the benchmark results: for accurate testing this should NEVER be changed!!!!
initial_path = os.path.join(os.path.dirname(__file__), "benchmark", "initial_grid.txt")
my_grid = np.loadtxt(initial_path, dtype=int, delimiter=' ')

#test that upcoming executions of the code will lead to the same result for a starting grid of 20x20, after 10 iterations
def test_lifegame3():
    my_ani = gameoflife_matilde_module.play_life_game_wplots(my_grid, 10)
    benchmark_path = os.path.join(os.path.dirname(__file__), "benchmark", "final_grid.txt")
    benchmark_final_grid = np.loadtxt(benchmark_path, dtype=int, delimiter=' ')
    this_final_grid = gameoflife_matilde_module.play_life_game(my_grid, 10)[-1]
    assert np.array_equal(this_final_grid, benchmark_final_grid)
