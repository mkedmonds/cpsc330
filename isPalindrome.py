# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 14:28:41 2021

@author: madne
"""

class Palindrome:
    
    def __init__(self, item):
        self.head = item
    
    def isPalindromeTest(self, str):
        
        lim = len(str) / 2
        
        for i in range(int(lim)):
            
            if str[i] != str[len(str) - i -1]:
                return False
        return True
            
    def isPalindrome(self):
 
        temp = self.head 
        
        listPal = []
        
        while(temp):
            
            listPal.append(temp.get_data())
            
            temp = temp.get_next()
            
        string1 = "".join(listPal)

        return self.isPalindromeTest(string1)
    
    
def ispalindrome(head):
     
    # Temp pointer
    slow = head
 
    # Declare a stack
    stack = []
     
    ispalin = True
 
    # Push all elements of the list
    # to the stack
    while slow != None:
        stack.append(slow.data)
         
        # Move ahead
        slow = slow.ptr
 
    # Iterate in the list again and
    # check by popping from the stack
    while head != None:
 
        # Get the top most element
        i = stack.pop()
         
        # Check if data is not
        # same as popped element
        if head.data == i:
            ispalin = True
        else:
            ispalin = False
            break
 
        # Move ahead
        head = head.ptr
         
    return ispalin
 

def isPalindrome(self):
        
        temp = self.head
        print("Temp: ", temp)
        
        isPal = True
        
        listPal = []
        
        while temp:
            
            listPal.append(temp.get_data())
            temp = temp.get_next()
            
        print("LIST: ", listPal)     
        
        while temp != None:
            print("LISTTEST: ", listPal)
            compare = listPal.pop();
            print("COMAPARE: ", compare, "- Temp: ", temp.get_data())
# =============================================================================
#             if temp.get_data() == compare:
#                 isPal = True
#                 
#             else:
#                 isPal = False
#                 
#             item = item.
# =============================================================================
        
        return isPal
        
        
        # Run loop from 0 to len/2
# =============================================================================
#         for i in range(0, int(len(str)/2)):
#             if str[i] != str[len(str)-i-1]:
#                 return False
#         return True
# =============================================================================
        