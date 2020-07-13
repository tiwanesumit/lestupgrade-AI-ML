# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 13:29:29 2020

@author: DELL
"""

a = int(input())
b = int(input())
z = a + b

print(z)

"""
Question 1 :
Research on whether addition, subtraction, multiplication, division, floor division and modulo
operations be performed on complex numbers. Based on your study, implement a Python
program to demonstrate these operations

"""
#addition
a = 2+3j
b = 5+6j

x = a+b
print(x)

#subtraction

x= a-b
print(x)

#multiplication

x =a*b
print(x)


#Question 2 : Research on range() functions and its parameters. Create a markdown cell and write in your own words (no copy-paste from google please) what you understand about it.
#Implement a small program of your choice on the same.
 
 
y = range(3, 6)
for t in y:
  print(t)


my_list = ['one', 'two', 'three', 'four', 'five']
my_list_len = len(my_list)
for i in range(0, my_list_len):
    print(my_list[i])
    
    
#Question 3: Consider two numbers. Perform their subtraction and if the result of subtraction is greater than 25,
#print their multiplication result else print their division result.    
    

x = 150
y = 10

sub = x-y
if(sub>25):
    print(x*y)
else:
    print(x/y)
    
    
#Question 4: Consider a list of 10 elements of integer values. If the number in the list is divisible by 2,
#print the result as "square of that number minus 2".    
 

list = [1, 2, 12, 22, 30, 40, 50, 67, 80, 10]

for i in list:
    #print(i)
    if(i%2==0):
        print(i*i-2)
        
        
#Question 5: Consider a list of 10 elements. Print all the elements in the list which are greater than 7 when that number is divided 2.
        
list1 = [1, 2, 12, 22, 33, 44, 55, 6, 8, 10]

for i in list1:
    if(i%2==0 and i>7):
        print(i) 
 
 
 
 
 
 
 