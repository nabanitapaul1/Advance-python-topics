# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 16:37:17 2023

@author: Nabanita Paul
"""

list1 =[1,2,3,54]
list2 =list1
list1
list2
list2[0]=30
list2
list1

## copy

list1 =[1,2,3,54]
list2 =list1.copy()
list2
list2[2]=90
list2
list1



list1 = [[1,23,4,5],[24,56,78,90]]
list2 = list1.copy()
list2
list2[1][1]=666
list2
list1

## Deep copy

import copy

list1 = [[1,23,4,5],[24,56,78,90]]
list2 = copy.deepcopy(list1)
list2
list2[1][1]=666
list2
list1
