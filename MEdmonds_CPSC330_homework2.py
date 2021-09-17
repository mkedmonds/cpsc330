# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 10:54:12 2021

@author: Madeline Edmonds
CPSC 330 Homework 2 Problems A, B, C
Last Edited: Spetember 16, 2021
"""

from node import Node

# =============================================================================
# Exercise A
# =============================================================================
class CharList:
    
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        
    
    def print_list(self):
        temp = self.head
        
        while(temp):
            temp.print_node()
            temp = temp.get_next()

# =============================================================================
# Exercise B
# =============================================================================
    def isPalindrome(self):
        temp = self.head
        list1 = [] # To turn the linked list into a normal array
        isPal = True #To check if the linked list is a palindrome
        
        while temp:
            
            # This loop will go through the linked list to add 
            # the nodes into an array
            
            list1.append(temp.get_data())
            temp = temp.get_next()
         
        temp = self.head
        
        # Loop through the array to see if the array value i 
        # matches the data value in the linked list.
        # If not, the isPal will be set to false and the fuction will return False
        # Otherwise, the function returns True.
        for i in list1[::-1]:
            
            if i != temp.get_data():
                
                isPal = False
            temp = temp.get_next()
            
        return isPal

# +++++++++++++++++++++++++++++++++++
# =============================================================================
# Four different strings were tested, two palindromes, two 
# not-Palidromes.
# =============================================================================
stringOne = "Bagels"
list1 = CharList()
for i in range(len(stringOne)):
    list1.add(stringOne[i])
    
list1.print_list()

print(list1.isPalindrome())


print("++++++++++")

stringTwo = "radar"
list2 = CharList()
for i in range(len(stringTwo)):
     list2.add(stringTwo[i])
     
list2.print_list()

print(list2.isPalindrome())

print("++++++++++")

stringThree = "luigi"
list3 = CharList()
for i in range(len(stringThree)):
     list3.add(stringThree[i])
     
list3.print_list()

print(list3.isPalindrome())

print("++++++++++")

stringFour = "MADAM"
list4 = CharList()
for i in range(len(stringFour)):
     list4.add(stringFour[i])
     
list4.print_list()

print(list4.isPalindrome())

# =============================================================================
# C. What change could be made to the class definition in Problem a. 
# to make your solution in Problem b. more efficient? Explain. What 
# is the Big-O upper bound? Hint: Think of how the palindrome 
# determination problem is solved for a regular string
# =============================================================================

# =============================================================================
# Currently my palidrome notation is O(n). If I wanted to make it 
# faster than maybe I could divide the list to be searched quickly.
# So, If in the class definition there could be a pointer value 
# where if I knew the middle point the time taken would be faster
# as my program would be analyzing two small lists rather than on 
# big list.
# =============================================================================
