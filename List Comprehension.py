# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 09:34:25 2023

@author: Nabanita Paul
"""

## List Comprehension is concise way of creating a list with for loop  inside a bracket

a_num_lst = [1,4,6,2,9,7,3]
cube_num_list = [i**3 for i in a_num_lst] 
cube_num_list ## Cube list

even_num_list =[i  for i in a_num_lst if i%2==0]
even_num_list
