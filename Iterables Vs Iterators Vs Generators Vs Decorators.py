# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 07:23:40 2024

@author: Nabanita Paul
"""

#Iterable--- A list is an iterable -- An object over which we can iterate the elements
a_list=[1,3,4,5,6]
for i in a_list:
    print(i)



#Iterator--- An  object which helps to iterate over another object

x=iter(a_list)

# With the next method we can get the elemnet of an iterator one by one
try:
    print(next(x))
except StopIteration:
    print("There is no element")
for i in x:
    print(i)

## **Iterator is an iterable but and iterable is not iterable.

#Generators ---- Its a function which uses an yield keyword for returning and itertors

import  types,collections

issubclass(types.GeneratorType, collections.Iterator)

def square(n):
    for i in range(n):
        yield i**2
x=square(3)
print(x)
next(x)
for i in x:
    
    print(i)

## Decarators--- Its a function which contains a function as a parameter of a function

#Closures--- Function  with in a function

def details():
    my_name='My Name is  John Doe'
    def more_details():
        print('Hi')
        print(my_name)
        print('I am from Austria')
    
    return more_details()
details()

 
    
def details2(a_func):
    my_name='My Name is  John Doe'
    def more_details():
        print('Hi')
        print(my_name)
        print(a_func([1,2,4,5]))
        print('I am from Austria')
    
    return more_details()
details2(len)

def details2(a_func):
    def more_details():
        print('Hi')
        a_func      
        print('I am from Austria')
    
    return more_details()
def name_details():
    print('My Name is John Doe')
details2(name_details())

@details2
def name_details():
    print('My Name is John Doe')
