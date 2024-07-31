# Baruch_CIS_Project2
This was my third project in my CIS 2300 "Programming and Computational Thinking" led by professor Sadat Chowdhury

# Project Description

Suppose that the letters of the English alphabet are assigned the following values: 

| Letter              | value |
|---------------------|-------|
| a,e,i,o,u,n,r,t,l,s | 1     |
| d,g                 | 2     |
| b,c,m,p             | 3     |
| f,h,v,w,y           | 4     |
| k                   | 5     |
| j,x                 | 8     |
| q, z                | 10    |


However, for the purpose of this project, if the letter is part of my unique 7-letter-word, increase the value of such letters by the largest number from my 5-digit-number. Thus, if my word is orchids, and my number is 12345, then my largest digit is 5, and o = 6, r = 6, c = 8, h = 9, i=6, d = 7, s = 6.

Let us define the value of a word as the sum of values of all its letters. Thus, the word "cat" has a value of c+a+t = 8+1+1 = 10.

Using a python program, determine the value of these three words:

value1: honorificabilitudinitatibus


value2: incomprehensibilities


value3: thyroparathyroidectomized

Afterwards, my program should do the following:

if value1 is greater than value2, display value1+value3


if value2 is greater than value1, display value2+value3


if value1 and value2 are the same (equal), display value3



Here is an outline of the program:

```python

# step 1: define values for all the letters that are needed
# make sure my own letters are increased by my largest digit
a = 1 
b = 3
c = 8 # note: increased up by 5
#...
z = 10

# step2: calculate the value of the words: 
# honorificabilitudinitatibus, incomprehensibilities,thyroparathyroidectomized

value1 = h + o # + (complete this)
value2 = i + n # + (complete this)
value3 = t + h # + (complete this)

# step 3: write logic that compares value1 with value2
# if value1 and value2 are same, print value3
# if value1 is greater than value2, print (value1+value3), otherwise print (value2+value3)

```
