#Reverse LL(Iterative)
"""
Given a linked list, reverse it iteratively.
You don't need to print the elements, just reverse the LL duplicates and return the head of updated LL.

Input format : Linked list elements (separated by space and terminated by -1)`
"""
Sample Input :
1 2 3 4 5 -1
Sample Output :
5 4 3 2 1

Solution :

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    def __init__(self):
        head = None
    prev = None
    current =head
    while(current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev
    return head

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head
def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

from sys import setrecursionlimit
setrecursionlimit(10000)
arr=list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
r=reverse(l)
printll(r)


#Midpoint of Linked list
"""
Given a linked list, find and return the midpoint.
If the length of linked list is even, return the first mid point.

Input format : Linked list elements (separated by space and terminated by -1)`
"""
Sample Input 1 :
1 2 3 4 5 -1
Sample Output 1 :
3

Sample Input 2 :
1 2 3 4 -1
Sample Output 2 :
2

Solution :

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def midpoint_linkedlist(head):
    slow=head
    fast=head
    while (fast.next!=None) and (fast.next.next!=None):
        slow=slow.next
        fast=fast.next.next
    return slow

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

arr=list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
node = midpoint_linkedlist(l)
if node:
    print(node.data)


#Merge two sorted LL
"""
Given two linked lists sorted in increasing order. 
Merge them in such a way that the result list is also sorted (in increasing order).
Try solving with O(1) auxiliary space (in-place). You just need to return the head of new linked list, 
don't print the elements.

Input format :
Line 1 : Linked list 1 elements of length n (separated by space and terminated by -1)
Line 2 : Linked list 2 elements of length m (separated by space and terminated by -1)

Output format :
Merged list elements (separated by space)
"""
Sample Input :
 2 5 8 12 -1
 3 6 9 -1
Sample Output :
 2 3 5 6 8 9 12

Solution :

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge(head1,head2):
    temp = None
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.data <= head2.data:
        temp = head1
        temp.next = merge(head1.next, head2)
    else:
        temp = head2
        temp.next = merge(head1, head2.next)
    return temp

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

from sys import setrecursionlimit
setrecursionlimit(50000)
arr1=list(int(i) for i in input().strip().split(' '))
arr2=list(int(i) for i in input().strip().split(' '))
l1 = ll(arr1[:-1])
l2 = ll(arr2[:-1])
l = merge(l1, l2)
printll(l)


#Code : Merge Sort
"""
Sort a given linked list using Merge Sort.
You don't need to print the elements, just sort the elements and return the head of updated LL.

Input format :
Linked list elements (separated by space and terminated by -1)

Output format :
Updated LL elements (separated by space)
"""
Sample Input :
1 4 5 2 -1
Sample Output :
1 2 4 5

Solution :

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def getMiddle(head):
    if (head == None):
        return head
    slow = head
    fast = head
    while (fast.next != None and fast.next.next != None):
        slow = slow.next
        fast = fast.next.next
    return slow

def sortedMerge(a, b):
    result = None
    if a == None:
        return b
    if b == None:
        return a
    if a.data <= b.data:
        result = a
        result.next = sortedMerge(a.next, b)
    else:
        result = b
        result.next = sortedMerge(a, b.next)
    return result

def mergeSort(head):
    if head == None or head.next == None:
        return head
    middle = getMiddle(head)
    nexttomiddle = middle.next
    middle.next = None
    left = mergeSort(head)
    right = mergeSort(nexttomiddle)
    sortedlist = sortedMerge(left, right)
    return sortedlist

def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

arr = list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
l = mergeSort(l)
printll(l)


#Find a node in LL (recursive)
"""
Given a linked list and an integer n you need to find and return index where n is present in the LL. 
Do this recursively.
Return -1 if n is not present in the LL.
Indexing of nodes starts from 0.

Input format :
Line 1 : Linked list elements (separated by space and terminated by -1)
Line 2 : Integer n

Output format :
Index
"""
Sample Input 1 :
3 4 5 2 6 1 9 -1
5
Sample Output 1 :
2

Sample Input 2 :
3 4 5 2 6 1 9 -1
6
Sample Output 2 :
4

Solution :

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findNode(head,number, index):
    if (head == None):
        return -1
    if (head.data == number) :
        return index
    return findNode(head.next,number, index+1)

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

from sys import setrecursionlimit
setrecursionlimit(11000)
arr=list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
numberToFind=int(input())
index = findNode(l,numberToFind, 0)
print(index)


#Even after Odd LinkedList
"""
Arrange elements in a given Linked List such that, all even numbers are placed after odd numbers. 
Respective order of elements should remain same.
Note: Input and Output has already managed for you. You don't need to print the elements, 
instead return the head of updated LL.

Input format:
Linked list elements (separated by space and terminated by -1)

Output format:
Print the elements of updated Linked list. 
"""
Sample Input 1 :
1 4 5 2 -1
Sample Output 1 :
1 5 4 2

Sample Input 2 :
1 11 3 6 8 0 9 -1
Sample Output 2 :
1 11 3 9 6 8 0

Solution :

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def arranged_LL(head):
    oddH=None
    oddT=None
    evenH=None
    evenT=None
    if head is None or head.next is None:
        return head
    while head!=None:
        if head.data%2==1:
            if oddH is None:
                oddH=head
                oddT=head
                head=head.next
            else:
                oddT.next=head
                oddT=oddT.next
                head=head.next
        else:
            if evenH is None:
                evenH=head
                evenT=head
                head=head.next
            else:
                evenT.next=head
                evenT=evenT.next
                head=head.next
    if oddH is not None:
        if evenH is not None:
            oddT.next=evenH
            evenT.next=None
        else:
            oddT.next=None
        return oddH
    else:
        evenT.next=None
        return evenH
def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

arr=list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
l = arranged_LL(l)
printll(l)


#Delete every N nodes
"""
Given a linked list and two integers M and N. Traverse the linked list such that you retain M nodes then delete next N nodes, 
continue the same until end of the linked list. That is, in the given linked list you need to delete N nodes after every M nodes.

Input format :
Line 1 : Linked list elements (separated by space and terminated by -1)
Line 2 : M
Line 3 : N
"""
Sample Input 1 :
1 2 3 4 5 6 7 8 -1
2
2
Sample Output 1 :
1 2 5 6

Sample Input 2 :
1 2 3 4 5 6 7 8 -1
2
3
Sample Output 2 :
1 2 6 7

Solution :

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def skipMdeleteN(head, M, N):
    if head is None:
        return

    t1 = head
    i = 0
    j = 0
    while i < M - 1:
        if t1 is not None:
            t1 = t1.next
        else:
            return
        i += 1

    while j < N:
        if t1.next is not None:
            t1.next = t1.next.next
        else:
            return
        j += 1

    t2 = t1.next

    skipMdeleteN(t2, M, N)
    return head

def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

arr = list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
m = int(input())
n = int(input())
l = skipMdeleteN(l, m, n)
printll(l)


#Swap two Node of LL
"""
Given a linked list, i & j, swap the nodes that are present at i & j position in the LL. 
You need to swap the entire nodes, not just the data.
Indexing starts from 0. You don't need to print the elements, just swap and return the head of updated LL.
Assume i & j given will be within limits. And i can be greater than j also.

Input format :
Line 1 : Linked list elements (separated by space and terminated by -1)
Line 2 : i and j (separated by space)
"""
Sample Input 1 :
3 4 5 2 6 1 9 -1
3 4
Sample Output 1 :
3 4 5 6 2 1 9

Sample Input 2 :
3 4 5 2 6 1 9 -1
2 4
Sample Output 2 :
3 4 6 2 5 1 9

Solution :

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def swap_nodes(head, i, j):
    curr = head
    prev = previ = curri = prevj = currj = None
    count = 0
    while curr != None:
        if count == i:
            previ = prev
            curri = curr
        elif count == j:
            prevj = prev
            currj = curr
        prev = curr
        curr = curr.next
        count += 1
    if (curri == None or currj == None):
        return

    if previ == None:
        head = currj
    else:
        previ.next = currj

    if prevj == None:
        head = curri
    else:
        prevj.next = curri

    curr = curri.next
    curri.next = currj.next
    currj.next = curr
    return head

    pass

def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

arr = list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
i, j = list(int(i) for i in input().strip().split(' '))
l = swap_nodes(l, i, j)
printll(l)


#kReverse
"""
Implement kReverse( int k ) in a linked list i.e. you need to reverse first K elements,
then reverse next k elements and join the linked list and so on.
Indexing starts from 0. If less than k elements left in the last, you need to reverse them as well. 
If k is greater than length of LL, reverse the complete LL.
You don't need to print the elements, just return the head of updated LL.

Input format :
Line 1 : Linked list elements (separated by space and terminated by -1)
Line 2 : k
"""
Sample Input 1 :
1 2 3 4 5 6 7 8 9 10 -1
4
Sample Output 1 :
4 3 2 1 8 7 6 5 10 9

Sample Input 2 :
1 2 3 4 5 -1
2
Sample Output 2 :
2 1 4 3 5

Sample Input 3 :
1 2 3 4 5 6 7 -1
3
Sample Output 3 :
3 2 1 6 5 4 7

Solution :

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def kReverse(head, n):
    current = head
    next = None
    prev = None
    count = 0
    while (current is not None and count < n):
        next = current.next
        current.next = prev
        prev = current
        current = next
        count += 1
    if next is not None:
        head.next = kReverse(next, n)
    return prev

def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Read the link list elements including -1
arr = list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
i = int(input())
l = kReverse(l, i)
printll(l)


#Bubble Sort (Iterative) LinkedList
"""
Sort a given linked list using Bubble Sort (iteratively). While sorting, you need to swap the entire nodes, 
not just the data.
You don't need to print the elements, just sort the elements and return the head of updated LL.

Input format : Linked list elements (separated by space and terminated by -1)`
"""
Sample Input :
1 4 5 2 -1
Sample Output :
1 2 4 5

Solution :

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def getMiddle(head):
    if (head == None):
        return head
    slow = head
    fast = head
    while (fast.next != None and fast.next.next != None):
        slow = slow.next
        fast = fast.next.next
    return slow

def sortedMerge(a, b):
    result = None
    if a == None:
        return b
    if b == None:
        return a
    if a.data <= b.data:
        result = a
        result.next = sortedMerge(a.next, b)
    else:
        result = b
        result.next = sortedMerge(a, b.next)
    return result

def mergeSort(head):
    if head == None or head.next == None:
        return head
    middle = getMiddle(head)
    nexttomiddle = middle.next
    middle.next = None
    left = mergeSort(head)
    right = mergeSort(nexttomiddle)
    sortedlist = sortedMerge(left, right)
    return sortedlist

def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Read the link list elements including -1
from sys import setrecursionlimit

setrecursionlimit(11000)
arr = list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = mergeSort(l)
printll(l)
