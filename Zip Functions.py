# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 00:22:13 2023

@author: Nabanita Paul
"""

list1 = ["A","B","C"]
list2=[1,2,3]


output = zip(list1,list2)
output

next(output)

for i,j in list(output):
    print(i,j)


list3 =['x','y','z']

output = zip(list1,list2,list3)

for i,j,l in list(output):
    print(i,j,l)

list1 = ["A","B","C","D"]

output = zip(list1,list2,list3)

for i,j,l in list(output):
    print(i,j,l)
    

## Dictionary 

dict1 ={"first_name" :"Amit","last_name":"Verma","Age":30}
dict2 ={"first_name" :"Deepak","last_name":"Sharma","Age":29}
dict1.items()

a_dict = zip(dict1.items(),dict2.items())

for i,j in a_dict:
    print(i,j)
for (i1,j1),(i2,j2) in a_dict:
    print(i1,j1)
    print(i2,j2)