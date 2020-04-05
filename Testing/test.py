
import os

import pandas as pd

import Configuration.config as config
import Model.maze as maze

config.load('./configuration/initialisation.yml')

def test_get_maze_dimension():
    m = maze.Maze()
    m.initialize(os.path.join(config.value['src']['data'], 'maze.csv'))
    
    assert maze.Maze.getMazeDimension(m) == (15, 15)
