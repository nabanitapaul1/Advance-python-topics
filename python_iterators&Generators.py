# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 23:27:14 2023

@author: Nabanita Paul
"""

# list 

a_list= [1,2,3,5,9]
for i in a_list:
    print(i)
    
# tuple 
a_tuple = (2,378,9)
for i in a_tuple:
    print(i)

# set
a_set ={23,45,60}
for i in a_set:
    print(i)

# dictionary

a_dict= {1:"One",2:"Two", 3:"Three",4:"Four"}
for k,v in a_dict.items():
    print(k," : ",v)

# string

a_string= "This is a string"

for a_word in a_string:
    print(a_word)
    

## use of iter and next methods

a_iter = iter(a_list)
a_iter

print(next(a_iter))


### using while loop
a_element = iter(a_list)
while True:
    try:
       print(next(a_element)) 
    except StopIteration:
        break

    
### generator

import math
def sqaure_root(n):
    for i in range(n):
        yield math.sqrt(i)

a_item=iter(sqaure_root(3))
print(next(a_item))

for i in sqaure_root(4):
    print(i)