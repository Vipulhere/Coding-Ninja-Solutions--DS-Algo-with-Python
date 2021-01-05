#Search In BST
"""
Given a BST and an integer k. Find if the integer k is present in given BST or not.
Return the node with data k if it is present, return null otherwise.
Assume that BST contains all unique elements.

Input Format :
Line 1 : Elements in level order form (separated by space)
(If any node does not have left or right child, take -1 in its place)
Line 2 : Integer k

Output Format :
Node with data k
"""
Sample Input 1 :
8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
2
Sample Output 1 :
2
Sample Input 2 :
8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
12
Sample Output 2 :
(empty)

Solution :

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def searchInBST(root, k):
    if root==None:
        return False
    if root.data==k:
        return root.data
    elif root.data>k:
        return searchInBST(root.left,k)
    elif root.data<k:
        return searchInBST(root.right,k)
    else:
        return False

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
k=int(input())
node=searchInBST(root, k)
if node:
    print(node)


#Elements Between K1 and K2
"""
Given a Binary Search Tree and two integers k1 and k2, 
find and print the elements which are in range k1 and k2 (both inclusive).
Print the elements in increasing order.

Input format :
Line 1 : Elements in level order form (separated by space)
(If any node does not have left or right child, take -1 in its place)
Line 2 : Two Integers k1 and k2

Output Format :
Required elements (separated by space)
"""
Sample Input :
8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
6 10
Sample Output :
6 7 8 10

Solution :

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def elementsInRangeK1K2(root, k1, k2):
    if root == None:
        return
    if k1 < root.data:
        elementsInRangeK1K2(root.left, k1, k2)
    if k1 <= root.data and k2 >= root.data:
        print(root.data, end=" ")
    if k2 > root.data:
        elementsInRangeK1K2(root.right, k1, k2)

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
k1, k2 = (int(i) for i in input().strip().split())
elementsInRangeK1K2(root, k1, k2)


#Construct BST
"""
Given a sorted integer array A of size n which contains all unique elements. 
You need to construct a balanced BST from this input array. Return the root of constructed BST.

Note : If array size is even, take first mid as root.

Input format :
Line 1 : Integer n (Size of array)
Line 2 : Array elements (separated by space)

Output Format :
BST elements (in pre order traversal, separated by space)
"""
Sample Input :
7
1 2 3 4 5 6 7
Sample Output :
4 2 1 3 6 5 7

Solution :

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructBST(lst):
    if not lst:
        return None
    if len(lst) % 2 != 0:
        mid = (len(lst)) // 2
        root = BinaryTreeNode(lst[mid])
        root.left = constructBST(lst[:mid])
        root.right = constructBST(lst[mid + 1:])

    else:
        mid = ((len(lst)) // 2) - 1
        root = BinaryTreeNode(lst[mid])
        root.left = constructBST(lst[:mid])
        root.right = constructBST(lst[mid + 1:])

    return root

def preOrder(root):

    if root == None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

n = int(input())
lst = [int(i) for i in input().strip().split()]
root = constructBST(lst)
preOrder(root)
