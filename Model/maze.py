import json
import os
import pandas as pd
import Configuration.config as config

from random import randint

config.load('./configuration/initialisation.yml')

class Maze:    
    WIDTH = 15
    HEIGTH = 15
    
    def __init__(self):
        self.dataframe = None
        self.number_items = json.load(open(os.path.join(config.value['src']['data'], 'number_items.json')))
    
    def data_from_csv(self, csv_file):
        self.dataframe = pd.read_csv(csv_file, sep=';', header=None, dtype=str)        
        
    def initialize(self, csv_file):        
        self.data_from_csv(csv_file)
        print('data loaded')
        
    def __repr__(self):
        return repr(self.dataframe)
     