import pytest
import numpy as np
import gameoflife_matilde_module


"""We want to implement a unit test and a regression test. Therefore, we will test if 
some function is doing what it is supposed to be doing (unit testing). Then, we will 
also test if some change in the code changed the way the code should work."""

#-------------------------------------------------------UNIT TESING-------------------------------------------------------

my_grid = np.random.randint(low = 0, high=2, size = (50,50))

#pretty lame test, but let's make sure it returns a grid with the same size
def test_lifegame():
    assert np.shape(gameoflife_matilde_module.life_game(my_grid)) == np.shape(my_grid)

#make sure a grid of only zeros returns a grid of only zeros
def test_lifegame2():
    assert np.array_equal(gameoflife_matilde_module.life_game(np.zeros(shape=(500,500))), np.zeros(shape=(500,500))) == True

#------------------------------------------------------REGRESSION TESTING----------------------------------------------------

#grid generated for the benchmark results: for accurate testing this should NEVER be changed!!!!
np.random.seed(0)
my_grid = np.random.randint(low = 0, high = 2, size = (20,20))

#test that upcoming executions of the code will lead to the same result for a starting grid of 20x20, after 10 iterations
def test_lifegame3():
    my_ani = gameoflife_matilde_module.play_life_game_wplots(my_grid, 10)
    my_ani.save( "/home/matildeg02/GameofLife/tests/life_game.mp4", writer="ffmpeg", fps=20)
    #regarding animations the only really possible test is to look at this and the one saved on benchmark side by side 
    benchmark_final_grid = np.loadtxt("benchmark/final_grid.txt", dtype=int, delimiter=' ')
    this_final_grid = gameoflife_matilde_module.play_life_game(my_grid, 10)[-1]
    assert np.array_equal(this_final_grid, benchmark_final_grid)