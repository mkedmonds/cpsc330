# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 09:37:25 2021

@author: madne
"""

class Solution(object):
   def isPalindrome(self, head):
      fast,slow = head,head
      rev = None
      flag = 1
      if not head:
         return True
      while fast and fast.next:
         if not fast.next.next:
            flag = 0
            break
         fast = fast.next.next
         temp = slow
         slow = slow.next
         temp.next = rev
         rev = temp
      #print(fast.val)
      fast = slow.next
      slow.next = rev
      if flag:
         slow = slow.next
      while fast and slow:
         if fast.data != slow.data:
            return False
         fast = fast.next
         slow = slow.next
      return True