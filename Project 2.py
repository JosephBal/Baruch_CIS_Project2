# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 17:45:57 2023

@author: Admin
"""


# step 1: define values for all the letters that are needed
# make sure my own letters are increased by my largest digit
a = 9 
b = 3
c = 3
d = 2
e = 9
f = 4
g = 10
h = 4
i = 1
j = 8
k = 5
l = 1
m = 3
n = 1
o = 9
p = 3
q = 10
r = 9
s = 9
t = 1
u = 1
v = 4
w = 4
x = 8
y = 4
z = 10

# step2: calculate the value of the words: 
# honorificabilitudinitatibus, incomprehensibilities,thyroparathyroidectomized

value1 = h + o + n + o + r + i + f + i + c + a + b + i + l + i + t + u + d + i + n + i + t + a + t + i + b + u + s
value2 = i + n + c + o + m + p + r + e + h + e + n + s + i + b + l + i + t + i + e + s
value3 = t + h + y + r + o + p + a + r + a + t + h + y + r + o + i + d + e + c + t + o + m + i + z + e + d

# step 3: write logic that compares value1 with value2
# if value1 and value2 are same, print value3
# if value1 is greater than value2, print (value1+value3), otherwise print (value2+value3)

if value1 == value2:
    print(value3)
if value1 > value2:
    print(value1 + value3)
if value1 < value2:
    print(value2 + value3)
