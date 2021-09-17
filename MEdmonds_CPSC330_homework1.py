# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 10:07:09 2021

@author: Madeline Edmonds

CPSC 330: Data Structures and Algorithms

Homework 1

Last Edited: 31 August 2021
"""

# =============================================================================
# Exercise A
#
# It would be O(n) bacause what the genie is doing is a searching 
# process. The genie is going to have to look at every value, search for 
# their duplicates(if any) and return all indices. Asuming the genie is 
# working at the best case senario, then O(N) is the most efficient
#
# =============================================================================

# =============================================================================
# Exercise B
#
# If the genie is working at time proportional, then it will take O(n^2) to 
# search the array and lookup any duplicates whiles also returning all 
# indices.
#
# =============================================================================

# =============================================================================
# ORIGINAL CODE
# =============================================================================
def bubble_sort(a_list):
    for i in range(len(a_list)-1):
        for j in range(len(a_list)-1 - i):
            if(a_list[j]>a_list[j+1]):
                temp = a_list[j]
                a_list[j] = a_list[j+1]
                a_list[j+1] = temp 
    
    return a_list

listOne = [2,15, 12, 6, 8]
listTwo = [9, 4, 0, 2, 78, 8]

print(bubble_sort(listOne))
print(bubble_sort(listTwo))

print("---------------")

# =============================================================================
# MODIFIED CODE
# =============================================================================
def bubble_sort_Mod(a_list):
    
    changes = True ## A checkpoint to catch any changes in the code
    
    for i in range(len(a_list) - 1):
        
        ## If the list values are already sorted 
        ## there doesnt need to be a check for changes so the loop 
        ## doesn't proceed
        if not changes:
            break
        
        changes = False 
        ## If there are any changes we need to change the checkpoint 
        ## to false so it can be changed in the sorting portion if 
        ## there are any swaps. If none, the loop will skip over to 
        ## the next values.
        
        ## The sorting portion works as normal
        for j in range(len(a_list)-1 - i):
            if(a_list[j]>a_list[j+1]):
                temp = a_list[j]
                a_list[j] = a_list[j+1]
                a_list[j+1] = temp
                changes = True ## "changes" is set to True to continue the loop
        
    return a_list


listThree = [2,15, 12, 6, 8]
listFour = [9, 4, 0, 2, 78, 8]

print(bubble_sort_Mod(listThree))
print(bubble_sort_Mod(listFour))

# =============================================================================
#  Exercise D
#
# The worst case senario of the bubble sort code would be that every 
# value would need to be swapped. So, the Big-O would be O(n^2)
#
# =============================================================================

# =============================================================================
# Exercise E
#
# The average case would still be O(n^2) because there would still be 
# values that needs to be sorted so the time taken would be the same.
# =============================================================================
