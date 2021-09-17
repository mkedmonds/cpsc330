# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 10:54:12 2021

@author:Madeline Emdonds
CPSC 330 Homework 2 D, E
Last Edited: Spetember 16, 2021
"""
from node import Node

class List:

    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        
# =============================================================================
# Exercise D      
# =============================================================================
    def reverse(self):
        past = None
        current = self.head
        
        while current is not None:
            nextVal = current.next
            current.next = past
            past = current
            current = nextVal
            
        self.head = past
  
# =============================================================================
# Exercise E
# =============================================================================
    def deleteMiddleNode(self):
        #list is empty
        if(self.head == None):
            print('List is empty')
            return
        
# =============================================================================
#         Get the midpoint of the size of the list. From there, 
#         locate the node in that midpoint value and remove it 
#         from the list. Then take the remaining values and 
#         ensure the list is closed
# =============================================================================
        temp = self.head
        midpoint = int(self.size() / 2)
        
        for i in range(midpoint):
            
            cur = temp 
            temp = temp.get_next()
            
        if cur != None:
            cur.next = temp.get_next()
            
            temp = None
            
        temp_prv = self.head #previous pointer
        temp_cur = temp_prv.get_next() #current pointer
        
        while(temp_cur):
            
            temp_prv = temp_prv.get_next()
            temp_cur = temp_cur.get_next()
        
    def print_list(self):
        temp = self.head
        
        while(temp):
            temp.print_node()
            temp = temp.get_next()
            
    # Gets the size of the linked list
    def size(self):
        temp = self.head
        count = 0
        
        while(temp):
            count +=1 
            temp = temp.get_next()
            
        return count
        
ll = List()

ll.add(5)
ll.add(12)
ll.add(7)

print("List")
ll.print_list()

print()

# =============================================================================
# D. Add a method to the classic List class we discussed in class 
# that reverses the list. That is, if the original list is 
# A -> B -> C, all of the list’s links should change so that 
# C -> B -> A. Make your solution as efficient as possible. You may 
# modify the List class to fit your needs
# 
# =============================================================================
print("Reversed")
ll.reverse()
ll.print_list()

# =============================================================================
# E. Let’s say you have access to a node from somewhere in the middle of
# a classic linked list, but not the linked list itself (the head 
# node is not available). That is, you have a variable that points to 
# an instance of Node, but you don’t have access to the LinkedList 
# instance. In this situation, if you follow this node’s link, you 
# can find all the items from this middle node until the end, but 
# you have no way to find the nodes that precede this node in the 
# list. Write code that will effectively delete this node from the 
# list. The entire remaining listshould remain complete, with only 
# this node removed.
# =============================================================================

print()

print("Delete Middle Node")
listOne = List()

string1 = "Alice"

for i in range(len(string1)):
     listOne.add(string1[i])
     
listOne.print_list()
print("Size: ", listOne.size())
print()
listOne.deleteMiddleNode()
listOne.print_list()
print("Size: ", listOne.size())

print("++++++++++++")

listTwo = List()

string2 = "Morgana"

for i in range(len(string2)):
     listTwo.add(string2[i])
     
listTwo.print_list()
print("Size: ", listTwo.size())
print()
listTwo.deleteMiddleNode()
listTwo.print_list()
print("Size: ", listTwo.size())