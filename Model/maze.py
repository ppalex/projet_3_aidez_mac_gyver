import json
import os
from csv import reader
from random import randint

import pandas as pd

import Configuration.config as config
from Model.board import Cell
from Model.gate import Gate
from Model.guardian import Guardian
from Model.item import Ether, Needle, Tube
from Model.wall import Wall

config.load('./configuration/initialisation.yml')

class Maze:    
    WIDTH = 15
    HEIGTH = 15
    
    def __init__(self):
        
        self.map = []        
        self.walls = []
        self.gates = []
        self.items = []
        self.guardians = []       
        
        self.number_items = json.load(open(os.path.join(config.value['src']['data'], 'number_items.json')))    
    
    def __repr__(self):        
        width, height = self.get_map_size()
        map = ""
        for row in range(width):
            for col in range(height):
                map += self.map[row][col]
            map += '\n'
        return map
    
    
    def data_from_csv(self, csv_file):
        with open(csv_file, 'r') as read_obj:
            csv_reader = reader(read_obj, delimiter=';')
            
            self.map = list(csv_reader)               
    
      
    def initialize(self, csv_file):        
        self.data_from_csv(csv_file)
        print('data loaded') 
        self.generate_maze()
        print('maze generated')
        self.put_random_items()
        print('random items done')      
        
    def get_map_size(self):
        return (len(self.map),len(self.map[0]))
    

    def generate_maze(self):
        
        width, height = self.get_map_size()
                                
        for row in range(width):        
            for col in range(height):               
                    if self.map[row][col] == '1':
                        
                        x = row * Cell.WIDTH
                        y = col * Cell.HEIGHT   
                        self.walls.append(Wall(x, y))
                    
                    elif self.map[row][col] == '9':                    
                        x = row * Cell.WIDTH
                        y = col * Cell.HEIGHT
                        self.gates.append(Gate(x, y))
                        
                    elif self.map[row][col] == 'G':                    
                        x = row * Cell.WIDTH
                        y = col * Cell.HEIGHT
                        self.guardians.append(Guardian(x, y))
                        
                         
    def put_random_items(self):
        
        width, height = self.get_map_size()
                     
        for key, value in self.number_items.items():            
            for n in range(value):
                x = randint(0, width - 1)
                y = randint(0, height - 1)               
                
                while not self.map[x][y] == '0':
                    x = randint(0, width - 1)
                    Y = randint(0, height - 1)             
         
                if key == "Needle":
                    self.map[x][y] = 'N'
                    self.items.append(Needle(x, y)) 
                elif key == "Tube":
                    self.map[x][y] = 'T'
                    self.items.append(Tube(x, y)) 
                elif key == "Ether":
                    self.map[x][y] = 'E'
                    self.items.append(Ether(x, y))        