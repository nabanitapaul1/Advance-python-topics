# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 23:41:49 2023

@author: Nabanita Paul
"""

class car():
    def __init__(self,windows,doors,engine_type):
        self.windows=windows
        self.doors =doors
        self.engine_type =engine_type
    def enable_ai(self):
        return "The car is AI enabled"
car

dir(car)  ## This will show all the magic methods in python inbulit
car1=car(4,4,'Petrol')
car1
print(car1)

## Magic methods
dir(car1)
class car():
    def __new__(self,windows,doors,engine_type):
        print( "This object is being initialized")
    def __init__(self,windows,doors,engine_type):
        self.windows=windows
        self.doors =doors
        self.engine_type =engine_type
    def __str__(self):
        return "This is a string method"
    def __sizeof__(self):
        return "This represents size"
    def enable_ai(self):
        return "The car is AI enabled"

car1=car(4,4,'Petrol')
car1
print(car1)


