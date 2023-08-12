# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 23:08:37 2023

@author: Nabanita Paul
"""
## Eval 

eval("10+10")

eval('2**2')

def square(n):
    return n**2
eval('square(5)')

eval('25>20')

a= 24
b=37

eval('a+b',{"a":a,"b":b})
