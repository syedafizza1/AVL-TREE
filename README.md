# AVL-TREE
## WHAT IS AVL TREE?
AVL tree is a binary search tree in which the difference of heights of left and right sub trees of any node is less than or equal to one. The technique of balancing the height of binary trees was developed by Adelson,Velskii, and Landi. HERE N = Node.
## KINDS OF ROATATION
Right-Right ---> N is a right ---> child of its parent X and N is not left-heavy ---> (BalanceFactor(N)≥ 0).

Left-Left ---> N is a left ---> child of its parent X and N is not right-heavy ---> (BalanceFactor(N)≤ 0).

Right-Left ---> N is a right ---> child of its parent X and N is left-heavy ---> (BalanceFactor(N) = −1).

Left-Right ---> N is a left child of its parent X and N is right-heavy ---> (BalanceFactor(N) = +1).

## TIME COMPLEXITY 
Time complexity of AVL delete is O(Log n).

Time complexity of AVL insert is O(Logn).

## TIME COMPLEXITY with respect to Height:
The rotation operations (left and right rotate) take constant time as only few pointers are being changed there. 

Updating the height and getting the balance factor also take constant time. 

So the time complexity of AVL delete remains same as BST delete which is O(h) where h is height of the tree. 

Since AVL tree is balanced, the height is O(Logn). 

The rotation operations (left and right rotate) take constant time as only a few pointers are being changed there. 

Updating the height and getting the balance factor also takes constant time. So the time complexity of AVL insert remains same as BST insert which is O(h) where h is the height of the tree. 

Since AVL tree is balanced, the height is O(Logn). .

## GROUP MEMBERS:
Mahnoor Nadeem

Abdul Wahab Amir

Syeda Fizza Jaffery



  
 

