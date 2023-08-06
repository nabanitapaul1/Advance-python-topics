# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 18:51:56 2023

@author: Nabanita Paul
"""

# Assert Statement

## to check if the given logical sattement is true or false
## the program execution proceeds if only the assert statement is true and raises
## AssertionError if the assert statement is false

a_num=10
assert a_num>=10
assert a_num>10

try:
    a_num =int(input("Enter a Even Number"))
    assert a_num%2==0
    print("The number is even")
        
        
except AssertionError:
    print("Please Enter a Even Number")
    
def a_fun():
    return ("Hello")

a_fun()
a = a_fun()
a
del a_fun
a
