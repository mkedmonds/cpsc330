# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 10:08:11 2021

@author: madne
"""

class Palindrome:
    def isPalindrome(head):
        temp = head
        list1 = []
        
        while temp:
            
            list1.append(temp.get_data())
            temp = temp.get_next()
            
        return list1