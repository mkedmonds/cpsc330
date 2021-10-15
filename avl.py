# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 15:23:16 2021

@author: Madeline Edmonds
CPSC 330 Homework 4

Last Edited: Thursday Oct 14 2021
"""
from treenodeclass import TreeNode
import random

class AVLTree:
    def __init__(self):
        self.root = None
        self.size = 0
# =============================================================================
# New instances for AVL counting        
# =============================================================================
        self.numLeft = 0
        self.numRight = 0
        self.height = 1
        

    def num_nodes(self):
        return self.size
    
# =============================================================================
# Return the number by left + right rotations
# =============================================================================
    def numRotate(self):
        return self.numLeft + self.numRight
    
    
    
    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        
        self.size = self.size + 1
    
    def _put(self, key, value, current_node):
        if key < current_node.key:
            if current_node.left_child:
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, value, parent=current_node)
                self.updateBalance(current_node.left_child)
        else:
            if current_node.right_child:
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, value, parent=current_node)
                self.updateBalance(current_node.right_child)       
# =============================================================================
# UPDATE: Height of the AVL Tree
# =============================================================================
        current_node.height = max(self.getHeight(current_node.left_child), self.getHeight(current_node.right_child))
                
       
    def updateBalance(self,node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.is_left_child():
                node.parent.balanceFactor += 1
            elif node.is_right_child():
                node.parent.balanceFactor -= 1
            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)
                
    def rebalance(self,node):
        if node.balanceFactor < 0:
            if node.right_child.balanceFactor > 0:
                self.rotateRight(node.right_child)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.left_child.balanceFactor < 0:
                self.rotateLeft(node.left_child)
                self.rotateRight(node)
            else:
                self.rotateRight(node)
                
    def rotateLeft(self,rotRoot):
        newRoot = rotRoot.right_child
        rotRoot.right_child = newRoot.left_child
        if newRoot.left_child != None:
            newRoot.left_child.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.is_root():
            self.root = newRoot
        else:
            if rotRoot.is_left_child():
                rotRoot.parent.left_child = newRoot
            else:
                rotRoot.parent.right_child = newRoot
        newRoot.left_child = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)
# =============================================================================
# UPDATE: Num of left rotations by one and updating the height of the tree
# =============================================================================
        self.numLeft +=1
        rotRoot.height = 1 + max(self.getHeight(rotRoot.left_child),self.getHeight(rotRoot.right_child))
        newRoot.height = 1 + max(self.getHeight(newRoot.left_child),self.getHeight(newRoot.right_child))
        
        
    def rotateRight(self,rotRoot):
        
        newRoot = rotRoot.left_child
        rotRoot.left_child = newRoot.right_child        
        if newRoot.right_child != None:
            newRoot.right_child.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.is_root():
            self.root = newRoot
        else:
            if rotRoot.is_right_child():
                rotRoot.parent.right_child = newRoot
            else:
                rotRoot.parent.left_child = newRoot
        newRoot.right_child = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

# =============================================================================
# UPDATE: Num of right rotations by one and updating the height of the tree
# =============================================================================
        self.numRight = self.numRight + 1
        newRoot.height = 1 + max(self.getHeight(rotRoot.left_child),self.getHeight(rotRoot.right_child))
        rotRoot.height = 1 + max(self.getHeight(newRoot.left_child),self.getHeight(newRoot.right_child))
         
# =============================================================================
# Return the height of the AVL Tree
# =============================================================================
    def getHeight(self, root):
        if not root:
            return 0
        return root.height
        
    
        


# =============================================================================
# TESTING AVL TREE
# avl1 = AVLTree()
# 
# avl1.put(4, 2)
# avl1.put(13, 3)
# avl1.put(41, 12)
# avl1.put(3, 6)
# avl1.put(24, -5)
# avl1.put(-3, 23)
# 
# print(avl1.num_nodes())
# 
# print(avl1.get(41))
# =============================================================================

avl2 = AVLTree()
avlList = random.sample(range(1,1001), 1000) #Generate a radom unique array of 1000 numbers
# =============================================================================
# Add the numbers to the list
# =============================================================================
# =============================================================================
# root = None
# =============================================================================
for i in range(1000):
    avl2.put(0, avlList[i])

# =============================================================================
# Displays what numbers went into the AVLTree
# print(avlList)
# =============================================================================

# =============================================================================
# Displays the Number of Rotations, Nodes, and Height of tree
# =============================================================================
print(avl2.numRotate())
print(avl2.num_nodes())
print(avl2.getHeight(avl2))
