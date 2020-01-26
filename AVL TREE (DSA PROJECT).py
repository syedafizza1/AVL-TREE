#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        self.height=1

class AVL_TREE:
    def __init__(self):
        self.root=None
    
    def Insert(self,key):
        self.root=self.__Insert(self.root,key)
    
    def __Insert(self,root,key):
        if root==None:
            root=Node(key)
        elif key<root.value:
            root.left=self.__Insert(root.left,key)
        else:
            root.right=self.__Insert(root.right,key)
        
        # TO UPDATE THE HEIGHT
        root.height=1+max(self.__Height(root.left),self.__Height(root.left))
        
        # TO GET THE BALANCE FACTOR
        balance_factor=self.__balance_factor(root)
        
        #CASE 1: LEFT LEFT ROTATION
        if balance_factor > 1 and key < root.left.value: 
            return self.RIGHT_ROTATE(root)
        
        # CASE 2: LEFT RIGHT ROTATION
        if balance_factor > 1 and key > root.left.value: 
            root.left = self.LEFT_ROTATE(root.left) 
            return self.RIGHT_ROTATE(root) 
        
        #CASE 3: RIGHT RIGHT ROTATION
        if balance_factor < -1 and key > root.right.value: 
            return self.LEFT_ROTATE(root) 
        
        # CASE 4: RIGHT LEFT ROTATION
        if balance_factor < -1 and key < root.right.value: 
            root.right = self.RIGHT_ROTATE(root.right) 
            return self.LEFT_ROTATE(root) 
        return root 
    
    def __Height(self, root):#getting height
        if root==None:
            return 0
        else:
            return root.height
    
    def __balance_factor(self, root):
        if root==None: 
            return 0
        else:
            return self.__Height(root.left)-self.__Height(root.right)
    
    def LEFT_ROTATE(self,a):
        b=a.right 
        Sub_T2 = b.left 
        
        # PERFOM ROTATION PROCESS
        b.left =a
        a.right=Sub_T2 
        
        # Update heights 
        a.height = 1 + max(self.__Height(a.left),self.__Height(a.right)) 
        b.height = 1 + max(self.__Height(b.left),self.__Height(b.right)) 
        
        # Return the new root 
        return b 
    
    def RIGHT_ROTATE(self, a): 
        b= a.left 
        SUB_T3=b.right 
  
        # Perform rotation 
        b.right=a
        a.left =SUB_T3 
        
        # UPDATE HEIGHT
        a.height =1 + max(self.__Height(a.left),self.__Height(a.right)) 
        b.height =1 + max(self.__Height(b.left),self.__Height(b.right))
        
        # RETURN THE NEW NODE: 
        return b 
    
    def Preorder(self):
        return self.__Preorder(self.root)
    
    def __Preorder(self,root):
        if not root: 
            return
        print("{} ".format(root.value),end=" ")
        self.__Preorder(root.left) 
        self.__Preorder(root.right) 
    
    def Inorder(self):
        return self.__Inorder(self.root)
    
    def __Inorder(self,root):
        if not root: 
            return
        self.__Inorder(root.left) 
        print("{} ".format(root.value),end=" ")
        self.__Inorder(root.right) 
    
    def Postorder(self):
        return self.__Postorder(self.root)
    
    def __Postorder(self,root):
        if not root: 
            return
        self.__Postorder(root.left) 
        self.__Postorder(root.right) 
        print("{} ".format(root.value),end=" ")
    
    def findmin(self): 
        x=self.__findmin(self.root)
        return x.value
    
    def __findmin(self,root):
        while root is not None:
            if root.left is None:
                break
            root=root.left
        return root 
    
    def delete(self,key):
        x=self.__delete(self.root,key)
        return x
    
    def __delete(self,root,key):
        # BST delete 
        if not root: 
            return root 
        elif key < root.value: 
            root.left = self.__delete(root.left, key) 
  
        elif key > root.value: 
            root.right = self.__delete(root.right, key) 
  
        else: 
            if root.left is None: 
                temp = root.right 
                root = None
                return temp 
  
            elif root.right is None: 
                temp = root.left 
                root = None
                return temp 
  
            temp = self.__findmin(root.right) 
            root.value = temp.value 
            root.right = self.__delete(root.right,temp.value) 
        if root is None: 
                return root 
  
       #Update the height of ancestor  
        root.height = 1 + max(self.__Height(root.left), self.__Height(root.right)) 
  
        #the balance factor 
        balance = self. __balance_factor(root) 
  
        #  If the node is unbalanced,then try out the 4 cases 
        
        # Case 1 - Left Left 
        if balance > 1 and self. __balance_factor(root.left) >= 0: 
            return self.RIGHT_ROTATION(root) 
        
        # Case 2 - Right Right 
        if balance < -1 and self.__balance_factor(root.right) <= 0: 
            return self.LEFT_ROTATE(root) 
        
        # Case 3 - Left Right 
        if balance > 1 and self. __balance_factor(root.left) < 0: 
            root.left = self.LEFT_ROTATION(root.left) 
            return self.RIGHT_ROTATION(root) 
        
        # Case 4 - Right Left 
        if balance < -1 and self. __balance_factor(root.right) > 0: 
            root.right = self.RIGHT_ROTATION(root.right) 
            return self.LEFT_ROTATION(root) 
  
        return root 
    
         
avl_tree=AVL_TREE()
avl_tree.Insert(4)
avl_tree.Insert(2)
avl_tree.Insert(1)
avl_tree.Insert(5)
avl_tree.Insert(6)
avl_tree.Insert(9)
avl_tree.Insert(14)
avl_tree.Insert(11)
avl_tree.Insert(10)
avl_tree.Insert(20)
print("CONSTRUCTED AVL..........................................................")
print("PREORDER Traversal")
avl_tree.Preorder()
print("\nINOREDER Traversal")
avl_tree.Inorder()
print("\nPOSTORDER Traversal")
avl_tree.Postorder()
print("\nAFTER DELETION OF VALUE................................................. ")
avl_tree.delete(10)
print("PREORDER Traversal")
avl_tree.Preorder()
print("\nINOREDER Traversal")
avl_tree.Inorder()
print("\nPOSTORDER Traversal")
avl_tree.Postorder()


# In[ ]:




