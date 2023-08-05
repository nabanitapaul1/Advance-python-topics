# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 19:14:50 2023

@author: Nabanita Paul
"""

class car:
    pass

car1 = car()
car1.brand ='Audi'
car1.color='Black'
print(car1.brand)
print(car1.color)


class car:
    def __init__(self,brand, color):
        self.brand=brand
        self.color =color

car1 =car('Audi','Black')
car1.color

class car:
    def __init__(self,brand, color):
        self.brand=brand
        self.color =color
    def car_details(self):
        return "The brand of the car is {} and the color of the car is {}".format(self.brand,self.color)
        
car1 =car('Audi','Black')
car1.car_details()

## Inheritence
car1.windows=4
print(car1.windows)
class audi(car):
    def __init__(self,brand, color,windows):
        super().__init__(brand, color)
        self.windows =windows
    def  enable_ai(self):
        return "AI is enabled for Audi"

audi1=audi('011','Golden','4')
audi1.windows
audi1.enable_ai()
audi1.car_details()
audi1
audi


## Multiple Inheritence



class A:
    def method1(self):
        print("Class A method is called")

class B(A):
    def method1(self):
        print("Class B method is called")
    def method2(self):
        print("Class B method2 is called")
class C(A):
    def method1(self):
        print("Class C method is called")
class D(B,C):
    def method1(self):
        print("Class D method is called")
        
d =D()
d.method1()
d.method2()

A.method1(D)
B.method1(D)
C.method1(D)
D.method1(D)
class D(B,C):
    def method1(self):
        print("Class D method is called")
        A.method1(self)
        B.method1(self)
        C.method1(self)
d =D()
d.method1()

