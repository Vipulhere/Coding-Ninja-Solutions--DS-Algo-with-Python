#Sum Of Nodes
"""
Given a binary tree, find and return the sum of all nodes.

Input format :
Elements in level order form (separated by space).
If any node does not have left or right child, take -1 in its place.
"""
Sample Input :
5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1
Sample Output :
35

Solution :

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sumOfAllNodes(root):
    if (root == None):
        return 0
    return (root.data + sumOfAllNodes(root.left) + sumOfAllNodes(root.right))

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
print(sumOfAllNodes(root))


#Preorder Binary Tree
"""
Given a binary tree, print the preorder traversal of given tree.
Pre-order traversal is: Root LeftChild RightChild

Input format :
Elements in level order form (separated by space)
(If any node does not have left or right child, take -1 in its place)

Output Format :
Pre-order traversal, elements separated by space
"""
Sample Input :
8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
Sample Output :
8 3 1 6 4 7 10 14 13

Solution :

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preOrder(root):
    if root:
        print(root.data,end=" ")
        preOrder(root.left)
        preOrder(root.right)

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
preOrder(root)


#Postorder Binary Tree
"""
Given a binary tree, print the postorder traversal of given tree.
Post-order traversal is: LeftChild RightChild Root

Input format :
Elements in level order form (separated by space)
(If any node does not have left or right child, take -1 in its place)

Output Format :
Post-order traversal, elements separated by space
"""
Sample Input :
8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
Sample Output :
1 4 7 6 3 13 14 10 8

Solution :

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=' ')

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length <= 0 or levelorder[0] == -1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root

levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
postOrder(root)


#Nodes Greater Than X
"""
Given a Binary Tree and an integer x, find and return the count of nodes which are having data greater than x.

Input format :
Line 1 : Elements in level order form (separated by space)
(If any node does not have left or right child, take -1 in its place)
Line 2 : Integer x

Output Format :
count
"""
Sample Input :
8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
8
Sample Output :
3

Solution :

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def countNodesGreaterThanX(root, x):
    if root==None:
        return 0
    count=0
    if root.data>x:
        count=count+1
    countLeft=countNodesGreaterThanX(root.left,x)
    countRight=countNodesGreaterThanX(root.right,x)
    return count + countLeft + countRight

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

levelOrder = [int(i) for i in input().strip().split()]
x=int(input())
root = buildLevelTree(levelOrder)
print(countNodesGreaterThanX(root, x))


#Height Of Tree
"""
Given a binary tree, find and return the height of given tree.

Input format :
Nodes in the level order form (separated by space). If any node does not have left or right child, 
take -1 in its place

Output format :
Height
"""
Sample Input :
10
 9
4
-1
-1
 5
 8
-1
6
-1
-1
3
-1
-1
-1
Sample Output :
5

Solution :

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root == None:
        return 0
    else:
        lDepth = height(root.left)
        rDepth = height(root.right)
        if (lDepth > rDepth):
            return lDepth + 1
        else:
            return rDepth + 1

def buildLevelTree():
    root = BinaryTreeNode(int(input()))
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = int(input())
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = int(input())
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root

root = buildLevelTree()
print(height(root))


#Replace Node With Depth
"""
Given a a binary tree. Replace each of it's data with the depth of tree.
Root is at depth 0, change its value to 0 and next level nodes are at depth 1 and so on.
Print the tree after modifying in inorder fashion.

Input format :
Line 1 :  Elements in level order form (separated by space)
(If any node does not have left or right child, take -1 in its place)

Output Format :
Inorder traversal of modified tree.
"""
Sample Input :
     1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
Sample Output :
     2
     1
     2
     0
     2
     1
     2

Solution :

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def replaceWithDepth(root, level=0):
    if root == None:
        return
    root.data = level
    replaceWithDepth(root.left, level + 1)
    replaceWithDepth(root.right, level + 1)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length <= 0 or levelorder[0] == -1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root

levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
replaceWithDepth(root)
inorder(root)


#Is node present?
"""
Given a Binary Tree and an integer x, check if node with data x is present in the input binary tree or not. 
Return true or false.

Input format :
Line 1 : Elements in level order form (separated by space)
(If any node does not have left or right child, take -1 in its place)
Line 2 : Integer x

Output Format :
true or false
"""
Sample Input :
8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
7
Sample Output :
true

Solution :

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isNodePresent(root, x):
    if (root == None):
        return False
    if (root.data == x):
        return True
    res1 = isNodePresent(root.left, x)
    if res1:
        return True
    res2 = isNodePresent(root.right, x)
    return res2

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
x=int(input())
present=isNodePresent(root, x)
if present:
    print('true')
else:
    print('false')


#Nodes without sibling
"""
Given a binary tree, print all nodes that don’t have a sibling.

Edit : Print the elements in different lines. And order of elements doesn't matter.

Input format :
Elements in level order form (separated by space). If any node does not have left or right child, 
take -1 in its place.

Output format :
Print nodes separated by new line.
"""
Sample Input :
5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1
Sample Output :
9

Solution :

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def nodesWithoutSibling(root):
    if root == None:
        return
    if root.left is not None and root.right is not None:
        nodesWithoutSibling(root.left)
        nodesWithoutSibling(root.right)

    elif root.right is not None:
        print(root.right.data)
        nodesWithoutSibling(root.right)

    elif root.left is not None:
        print(root.left.data)
        nodesWithoutSibling(root.left)

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length <= 0 or levelorder[0] == -1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root

levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
nodesWithoutSibling(root)
