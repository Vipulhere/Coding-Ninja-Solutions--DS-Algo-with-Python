#Mirror Binary Tree
"""
Mirror the given binary tree. That is,
right child of every nodes should become left and left should become right.

Note : You don't need to print or return the tree, just mirror it.

Input format :
Line 1 : Elements in level order form (separated by space)
(If any node does not have left or right child, take -1 in its place)

Output format : Elements in level order form (Every level in new line)
"""
Sample Input 1:
1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
Sample Output 1:
1
3 2
7 6 5 4
Sample Input 2:
5 10 6 2 3 -1 -1 -1 -1 -1 9 -1 -1
Sample Output 2:
5
6 10
3 2
9

Solution :

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def mirrorBinaryTree(root):
    if root==None:
        return None
    else:
        temp = root
        mirrorBinaryTree(root.left)
        mirrorBinaryTree(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp

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

def printLevelATNewLine(root):

    if root==None:
        return
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ

levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
mirrorBinaryTree(root)
printLevelATNewLine(root)


#Diameter Of Binary Tree
"""
Given a Binary Tree, find and return the diameter of input binary tree.
Diameter is - largest count of nodes between any two leaf nodes in the binary tree 
(both the leaf nodes are inclusive).

Input format :
Elements in level order form (separated by space)
(If any node does not have left or right child, take -1 in its place)

Output Format :
diameter
"""
Sample Input :
8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
Sample Output :
7

Solution :

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def diameter(root):
    if root is None:
        return 0
    lheight = height(root.left)
    rheight = height(root.right)

    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)

    return max(lheight + rheight + 1, max(ldiameter, rdiameter))

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
print(diameter(root))


#Print Levelwise
"""
Given a binary tree, print the tree in level wise order.
For printing a node with data N, you need to follow the exact format -
        N:L:x,R:y
wherer, N is data of any node present in the binary tree. 
x and y are the values of left and right child of node N. Print -1. if any child is null.
There is no space in between.
You need to print all nodes in the level order form in different lines.

Input format :
Elements in level order form (separated by space)
(If any node does not have left or right child, take -1 in its place)
"""
Sample Input :
8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
Sample Output :
8:L:3,R:10
3:L:1,R:6
10:L:-1,R:14
1:L:-1,R:-1
6:L:4,R:7
14:L:13,R:-1
4:L:-1,R:-1
7:L:-1,R:-1
13:L:-1,R:-1

Solution :

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLevelWise(root):
    if root==None:
        return
    q = queue.Queue()

    q.put(root)
    while not q.empty():
        curr = q.get()
        print(curr.data, end=':')
        if curr.left!=None:
            print("L",end=":")
            print(curr.left.data,end=",")
            q.put(curr.left)
        else:
            print('L:-1,',end='')
        if curr.right!=None:
            print("R",end=":")
            print(curr.right.data,end="")
            q.put(curr.right)
        else:
            print('R:-1',end='')
        print()

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
printLevelWise(root)


#Construct Tree Using Inorder and Preorder
"""
Given Preorder and Inorder traversal of a binary tree, 
create the binary tree associated with the traversals.You just need to construct the tree and return the root.

Note: Assume binary tree contains only unique elements.

Input format :
Line 1 : n (Total number of nodes in binary tree)
Line 2 : Pre order traversal
Line 3 : Inorder Traversal

Output Format :
Elements are printed level wise, each level in new line (separated by space).
"""
Sample Input :
12
1 2 3 4 15 5 6 7 8 10 9 12
4 15 3 2 5 1 6 10 8 7 9 12
Sample Output :
1
2 6
3 5 7
4 8 9
15 10 12

Solution :

import queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTreePreOrder(preorder, inorder,inStrt, inEnd):
    if (inStrt > inEnd):
        return None
    tNode = Node(preorder[buildTreePreOrder.preIndex])
    buildTreePreOrder.preIndex += 1
    if inStrt == inEnd :
        return tNode
    inIndex = search(inorder, inStrt, inEnd, tNode.data)
    tNode.left = buildTreePreOrder(preorder, inorder, inStrt, inIndex-1)
    tNode.right = buildTreePreOrder(preorder, inorder, inIndex + 1, inEnd)
    return tNode

def search(arr, start, end, value):
    for i in range(start, end + 1):
        if arr[i] == value:
            return i

def printLevelATNewLine(root):

    if root==None:
        return
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ

n=int(input())
preorder = [int(i) for i in input().strip().split()]
inorder = [int(i) for i in input().strip().split()]
buildTreePreOrder.preIndex = 0
root = buildTreePreOrder(preorder, inorder,0, len(inorder)-1)
printLevelATNewLine(root)


#Construct Tree Using Inorder and PostOrder
"""
Given Postorder and Inorder traversal of a binary tree, create the binary tree associated with the traversals.
You just need to construct the tree and return the root.

Note: Assume binary tree contains only unique elements.

Input format :
Line 1 : n (Total number of nodes in binary tree)
Line 2 : Post order traversal
Line 3 : Inorder Traversal

Output Format :
Elements are printed level wise, each level in new line (separated by space).
"""
Sample Input :
8
8 4 5 2 6 7 3 1
4 8 2 5 1 6 3 7
Sample Output :
1
2 3
4 5 6 7
8

Solution :

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTreePostOrder(postorder, inorder):
    if(len(postorder)==0):
        return
    rootData=postorder[-1]
    root=BinaryTreeNode(rootData)
    for i in range(len(inorder)):
        if(inorder[i]==rootData):
            break
    lp=len(postorder)
    leftTree=buildTreePostOrder(postorder[:i],inorder[:i])
    rightTree=buildTreePostOrder(postorder[i:-1],inorder[i+1:])
    root.left=leftTree
    root.right=rightTree
    return root

def printLevelATNewLine(root):

    if root==None:
        return
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ

n=int(input())
postOrder = [int(i) for i in input().strip().split()]
inorder = [int(i) for i in input().strip().split()]
root = buildTreePostOrder(postOrder, inorder)
printLevelATNewLine(root)


#Create & Insert Duplicate Node
"""
Given a Binary Tree with N number of nodes, for each node create a new duplicate node, 
and insert that duplicate as left child of the original node.

Note : Root will remain same. 
So you just need to insert nodes in the given Binary Tree and no need to print or return anything.

Input format :
Elements in level order form (separated by space)
(If any node does not have left or right child, take -1 in its place)

Output Format :
Level order traversal of updated tree. (Every level in new line)
"""
Sample Input :
8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
Sample Output :
8
8 10
5 10
5 6
2 6 7
2 7

Solution :

import queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def NewNode(obj):
    new = Node(root)
    new.data = obj
    new.left = None
    new.right = None
    return new

def insertDuplicateNode(root):
    if root == None:
        return
    temp = Node(root)
    insertDuplicateNode(root.left)
    insertDuplicateNode(root.right)
    temp = root.left
    root.left = NewNode(root.data)
    root.left.left = temp
    pass

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length <= 0 or levelorder[0] == -1:
        return None
    root = Node(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = Node(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = Node(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root

def printLevelATNewLine(root):

    if root == None:
        return
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left != None:
                outputQ.put(curr.left)
            if curr.right != None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ

levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
insertDuplicateNode(root)
printLevelATNewLine(root)


#Min and max
"""
Given a binary tree, find and return the min and max data value of given binary tree.
Return the output as an object of PairAns class, which is already created.

Input format :
Elements in level order form (separated by space)
(If any node does not have left or right child, take -1 in its place)

Output Format :
Max and min (separated by space)
"""
Sample Input :
8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
Sample Output :
14 1

Solution :

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

INT_MIN = -2147483648
INT_MAX = 2147483647

def minMax(root):
    if root == None:
        return 2147483647, -2147483648

    leftmin, leftmax = minMax(root.left)
    rightmin, rightmax = minMax(root.right)
    minimum = min(leftmin, rightmin, root.data)
    maximum = max(leftmax, rightmax, root.data)

    return minimum, maximum

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
minimum, maximum = minMax(root)
print(maximum, minimum)


#Level order traversal
"""
Given a binary tree, print the level order traversal. Make sure each level start in new line.

Input format :
Elements in level order form (separated by space). If any node does not have left or right child, take -1 in its place.

Output Format :
Elements are printed level wise, each level in new line (separated by space).
"""
Sample Input :
5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1
Sample Output :
5
6 10
2 3
9

Solution :

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLevelATNewLine(root):
    if root is None:
        return
    q = []
    q.append(root)
    while q:
        count = len(q)
        while count > 0:
            temp = q.pop(0)
            print(temp.data, end = ' ')
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
            count -= 1
        print('')

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
printLevelATNewLine(root)


#Path Sum Root to Leaf
"""
Given a binary tree and a number k, 
print out all root to leaf paths where the sum of all nodes value is same as the given number k.

Input format :
Line 1 : Elements in level order form (separated by space)
(If any node does not have left or right child, take -1 in its place)
Line 2 : k

Output format : Print each path in new line, elements separated by space
"""
Sample Input 1 :
5 6 7 2 3 -1 1 -1 -1 -1 9 -1 -1 -1 -1
13
Sample Output 1 :
5 6 2
5 7 1

Solution :

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def rootToLeafPathsSumToK(root, k, lst):
    if root == None:
        return None
    if root.left == None and root.right == None and root.data == k:
        print(*lst, root.data)
        return
    lst.append(root.data)
    rootToLeafPathsSumToK(root.left, k - root.data, lst)
    rootToLeafPathsSumToK(root.right, k - root.data, lst)
    lst.pop()
    return

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
k = int(input())
rootToLeafPathsSumToK(root, k, [])


#Print nodes at distance k from node
"""
Given a binary tree, a node and an integer K, print nodes which are at K distance from the the given node.

Input format :
Line 1 : Elements in level order form (separated by space)
(If any node does not have left or right child, take -1 in its place)
Line 2 : Node
Line 3 : K

Output format : Answer nodes in different line
"""
Sample Input :
5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1
3
1
Sample Output :
9
6

Solution :

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printk(root, k):
    if root is None or k < 0:
        return
    if k == 0:
        print(root.data)
        return
    printk(root.left, k - 1)
    printk(root.right, k - 1)

def printknode(root, n, k):
    if root is None:
        return -1
    if root.data == n:
        printk(root, k)
        return 0

    ld = printknode(root.left, n, k)
    if ld != -1:
        if ld + 1 == k:
            print(root.data)
        else:
            printk(root.right, k - ld - 2)
        return ld + 1

    rd = printknode(root.right, n, k)
    if rd != -1:
        if rd + 1 == k:
            print(root.data)
        else:
            printk(root.left, k - rd - 2)
        return rd + 1

    return -1

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
n = int(input())
k = int(input())
ans = printknode(root, n, k)
