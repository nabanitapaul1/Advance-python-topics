# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 08:23:59 2023

@author: Nabanita Paul
"""

### Lambda Functions

## anonymous function, function with no name

add =lambda x,y :x+y

add(1,2)

add3 =lambda x,y,z :x+y+z
add3(45,68,79)


### Map Function

## To apply in all the elements of a list 


def  identify_number(a_num):
    
    if a_num%2 ==0:
        
        return "The {} is Even".format(a_num)
    else:
        return "The {} is odd".format(a_num)


## If we apply for loop in list it will take time
a_list = [34,58,32,57,34,21,779,30]
for i in a_list:
    
    print(identify_number(i))
    
# With Map Function
list(map(identify_number,a_list))


list(map(lambda a_num :a_num%2==0,a_list))


### Filter Function


def even_number(a_num):
    
    if a_num%2 ==0:
        return a_num
  
        
list(filter(even_number,a_list))

list(filter(lambda a_num:a_num%2==0,a_list))

### Reduce function

import functools
a_list = [1,6,9,11]
functools.reduce((lambda x,y :x+y),a_list) ## Sum of all the elements of a list
    
functools.reduce((lambda x,y :y if (y>x) else x),a_list) ## Greatest number of a list

