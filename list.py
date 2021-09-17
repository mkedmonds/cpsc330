# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 10:54:12 2021

@author:Madeline Emdonds
Editied by: 
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
        
    def reverse(self):
        past = None
        current = self.head
        
        while current is not None:
            nextVal = current.next
            current.next = past
            past = current
            current = nextVal
            
        self.head = past
        
    def print_list(self):
        temp = self.head
        
        while(temp):
            temp.print_node()
            temp = temp.get_next()
        
ll = List()

ll.add(5)
ll.add(12)
ll.add(7)

print("List")
ll.print_list()

print()

print("Reversed")
ll.reverse()
ll.print_list()