#Sum of all nodes
"""
Given a generic tree, count and return the sum of all nodes present in the given tree.

Input format :
Elements in level order form separated by space (as per done in class). Order is -
Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element

Output Format :
Sum of all nodes
"""
Sample Input :
10 3 20 30 40 2 40 50 0 0 0 0
Sample Output :
190

Solution :

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data)

def sumofNodes(tree):
    sum = tree.data
    for child in tree.children:
        sum += sumofNodes(child)
    return sum

    pass

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i < size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0, childCount):
            temp = treeNode(int(arr[i + j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
print(sumofNodes(tree))


#Node With Largest Data
"""
Given a generic tree, find and return the node with maximum data. 
You need to return the complete node which is having maximum data.
Return null if tree is empty.

Input format :
Elements in level order form separated by space (as per done in class). Order is - 
Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 

Output Format :
Node with largest data
"""
Sample Input :
10 3 20 30 40 2 40 50 0 0 0 0
Sample Output :
50

Solution :

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data)

def maxDataNode(tree):
    if tree == []:
        return None
    largest = tree.data
    for child in tree.children:
        if child.data > largest:
            largest = child.data
        MaxChild = maxDataNode(child)
        if MaxChild > largest:
            largest = MaxChild
    return largest

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i < size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0, childCount):
            temp = treeNode(int(arr[i + j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
print(maxDataNode(tree))


#Height Of Tree
"""
Given a generic tree, find and return the height of given tree.

Input format :
Elements in level order form separated by space (as per done in class). Order is - 
Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 

Output Format :
Height
"""
Sample Input :
10 3 20 30 40 2 40 50 0 0 0 0
Sample Output :
3

Solution :

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data)

def height(tree):
    if tree == []:
        return 0
    maxHeight = 0
    for child in tree.children:
        depth = height(child)
        if maxHeight < depth:
            maxHeight = depth
    return maxHeight + 1

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i < size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0, childCount):
            temp = treeNode(int(arr[i + j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
print(height(tree))


#Print Levelwise
"""
Given a generic tree, print the input tree in level wise order. ####For printing a node with data N, 
you need to follow the exact format -

                N:x1,x2,x3,...,xn

wherer, N is data of any node present in the binary tree. x1, x2, x3, ...., xn are the children of node N
There is no space in between.
You need to print all nodes in the level order form in different lines.

Input format :
Elements in level order form separated by space (as per done in class). Order is - 
Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 

Output Format :
Level wise print
"""
Sample Input :
10 3 20 30 40 2 40 50 0 0 0 0
Sample Output :
10:20,30,40
20:40,50
30:
40:
40:
50:


Solution :

import queue

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def printLevelWiseTree(tree):
    if tree==None:
        return
    q=queue.Queue()
    q.put(tree)
    while(not(q.empty())):
        temp=q.get()
        print(temp.data,end=":")
        for child in temp.children:
            q.put(child)
            if child==temp.children[len(temp.children)-1]:
                print(child,end="")
            else:
                print(child,end=",")
        print()
    return

    pass

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
printLevelWiseTree(tree)


#Contains x
"""
Given a generic tree and an integer x, check if x is present in the given tree or not. 
Return true if x is present, return false otherwise.

Input format :
Line 1 : Integer x
Line 2 : Elements in level order form separated by space (as per done in class). Order is - 
Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 

Output format :
true or false
"""
Sample Input 1 :
40
10 3 20 30 40 2 40 50 0 0 0 0
Sample Output 1 :
true
Sample Input 2 :
4
10 3 20 30 40 2 40 50 0 0 0 0
Sample Output 2:
false

Solution :

class treeNode:

    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data)

def containX(tree, x):
    if not tree:
        return False

    if tree.data == x:
        return True

    for child in tree.children:
        if containX(child, x):
            return True

    return False

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1

    while i < size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1

        for j in range(0, childCount):
            temp = treeNode(int(arr[i + j]))
            parent.children.append(temp)
            q.append(temp)

        i += childCount

    return root

x = int(input())
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
if containX(tree, x):
    print('true')
else:
    print('false')


#Count leaf Nodes
"""
Given a generic tree, count and return the number of leaf nodes present in the given tree.

Input format :
Elements in level order form separated by space (as per done in class). Order is - 
Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 

Output Format :
Count of leaf nodes
"""
Sample Input 1 :
10 3 20 30 40 2 40 50 0 0 0 0
Sample Output 1 :
4

Solution :

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    count=0
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        if childCount==0:
            count+=1

        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root,count

arr = list(int(x) for x in input().strip().split(' '))
tree,count = createLevelWiseTree(arr)
print(count)


#Node with maximum child sum
"""
Given a tree, find and return the node for which sum of data of all children and the node itself is maximum. 
In the sum, data of node itself and data of immediate children is to be taken.

Input format :
Line 1 : Elements in level order form separated by space (as per done in class). Order is - 
Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 

Output format :
Node with maximum sum.
"""
Sample Input :
5 3 1 2 3 1 15 2 4 5 1 6 0 0 0 0
Sample Output :
1

Solution :

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def maxSumUtil(root, resNode, maxsum):
    if root == None:
        return
    currsum = root.data
    count = len(root.children)
    for i in range(0, count):
        currsum += root.children[i].data
        resNode, maxsum = maxSumUtil(root.children[i], resNode, maxsum)
    if currsum > maxsum:
        resNode = root
        maxsum = currsum
    return resNode, maxsum

def maxSum(root):
    resNode, maxsum = treeNode(None), 0
    resNode, maxsum = maxSumUtil(root, resNode, maxsum)
    return resNode.data

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i < size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0, childCount):
            temp = treeNode(int(arr[i + j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

arr = list(int(x) for x in input().strip().split(' '))
root = createLevelWiseTree(arr)
print(maxSum(root))


#Structurally identical
"""
Given two Generic trees, return true if they are structurally identical 
i.e. they are made of nodes with the same values arranged in the same way.

Input format :
Line 1 : Tree 1 elements in level order form separated by space (as per done in class). 

Order is - 
            Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 
Line 2 : Tree 2 elements in level order form separated by space (as per done in class). 

Order is - 
            Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 

Output format :
true or false
"""
Sample Input 1 :
10 3 20 30 40 2 40 50 0 0 0 0
10 3 20 30 40 2 40 50 0 0 0 0
Sample Output 1 :
true
Sample Input 2 :
10 3 20 30 40 2 40 50 0 0 0 0
10 3 2 30 40 2 40 50 0 0 0 0
Sample Output 2:
false

Solution :

class treeNode:

    def __init__(self, data):
        self.data = data
        self.children = []

def isIdentical(tree1, tree2):
    if not tree1:
        if not tree2:
            return True
        return False

    if (tree1.data != tree2.data) or len(tree1.children) != len(tree2.children):
        return False

    for child1, child2 in zip(tree1.children, tree2.children):
        if not isIdentical(child1, child2):
            return False

    return True

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1

    while i < size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1

        for j in range(0, childCount):
            temp = treeNode(int(arr[i + j]))
            parent.children.append(temp)
            q.append(temp)

        i += childCount

    return root

arr1 = list(int(x) for x in input().strip().split(' '))
tree1 = createLevelWiseTree(arr1)
arr2 = list(int(x) for x in input().strip().split(' '))
tree2 = createLevelWiseTree(arr2)
if isIdentical(tree1, tree2):
    print('true')
else:
    print('false')


#Next larger
"""
Given a generic tree and an integer n. Find and return the node with next larger element in the Tree 
i.e. find a node with value just greater than n.
Return NULL if no node is present with the value greater than n.

Input Format :
Line 1 : Integer n
Line 2 : Elements in level order form separated by space (as per done in class). Order is - 
Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 

Output Format :
Node with value just greater than n.
"""
Sample Input 1 :
18
10 3 20 30 40 2 40 50 0 0 0 0
Sample Output 1 :
20
Sample Input 2 :
21
10 3 20 30 40 2 40 50 0 0 0 0
Sample Output 2:
30

Solution :

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def nextLargest(tree, n):
    if tree==[]:
        return
    Max=2147483647
    for child in tree.children:
        if child.data>n and child.data<Max:
            Max=child.data
        r=nextLargest(child,n)
        if r>n and r<Max:
            Max=r
    return Max

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

n = int(input())
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
print(nextLargest(tree, n))


#Replace with depth
"""
In a given Generic Tree, replace each node with its depth value. 
You need to just update the data of each node, no need to return or print anything.

Input format :
Line 1 : Elements in level order form separated by space (as per done in class). 
Order is - 
            Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 
"""
Sample Input 1 :
10 3 20 30 40 2 40 50 0 0 0 0
Sample Output 1 : (Level wise, each level in new line)
0
1 1 1
2 2

Solution :

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def replacewithDepth(tree, depth):

    if tree is None:
        return
    tree.data = depth
    for child in tree.children:
        replacewithDepth(child, depth + 1)
    return tree

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i < size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0, childCount):
            temp = treeNode(int(arr[i + j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

def printLevelAtNewLine(tree):
    q = [tree]
    newq = []
    while q:
        parent = q.pop(0)
        print(parent.data, end=' ')
        for child in parent.children:
            newq.append(child)
        if len(q) == 0:
            q = newq
            newq = []
            print()  # Move to next Line

arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
replacewithDepth(tree, 0)
printLevelAtNewLine(tree)
