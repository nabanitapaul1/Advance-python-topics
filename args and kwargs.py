# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 22:36:45 2023

@author: Nabanita Paul
"""

### *args ----Non-keyword argument

def add(*args):
    sum_item=0
    for a_item in args:
        sum_item = sum_item+a_item
    print(sum_item)

add(1,2,3,49,10)

def no_seq(st_no,*args):
    print("The 1st no is: ", st_no)
    for a_item in args:
        
        print("The next number is: ", a_item)
no_seq(1,2,3,49,10)

## *kwargs ---- Keyword argument

def myFun(**kwargs):
    for key,value in kwargs.items():
        print(key," : ",value)
myFun(first= "1",second ="2",third='3',fourth="4")

def myFun1(a_sentence,**kwargs):
    print(a_sentence)
    for key,value in kwargs.items():
        print(key," : ",value)
myFun1("This is my 1st sentence",first= "1",second ="2",third='3',fourth="4")


### In class ---*args

class car:
    
    def __init__(self,*args):
        
        self.color=args[0]
        self.speed=args[1]

audi =car('Black',150)
bmw= car('White',180)

print(audi.color)
print(bmw.speed)

class car1:
    
    def __init__(self,*kwargs):
        
        self.color=kwargs['c']
        self.speed=kwargs['s']

audi =car1(c='Black',s=150)
bmw= car1(c='White',s=180)

print(audi.color)
print(bmw.speed)


