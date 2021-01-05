#Length of LL
"""
For a given singly linked list of integers, find and return its length. Do it using an iterative method.

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
Then the test cases follow.
First and the only line of each test case or query contains elements of the singly linked list separated by a single space.

Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence,
would never be a list element.

Output format :
For each test case, print the length of the linked list.
Output for every test case will be printed in a seperate line.
"""
Sample Input 1 :
1
3 4 5 2 6 1 9 -1
Sample Output 1 :
7

Sample Input 2 :
2
10 76 39 -3 2 9 -23 9 -1
-1
Sample Output 2 :
8
0

Solution :

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findlength(head):
    if head == None:
        return 0

    if head.next == None:
        return 1

    return findlength(head.next) + 1

def ll(arr):

    if arr == []:
        return None

    head = Node(arr[0])
    last = head

    for data in arr[1:]:
        last.next = Node(data)
        last = last.next

    return head

from sys import setrecursionlimit
setrecursionlimit(11000)

arr = list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
len = findlength(l)
print(len)


#Print ith node
"""
For a given a singly linked list of integers and a position 'i', print the node data at the 'i-th' position.

Note :
Assume that the Indexing for the singly linked list always starts from 0.
If the given position 'i',  is greater than the length of the given singly linked list, then don't print anything.

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. 
Then the test cases follow.
The first line of each test case or query contains the elements of the singly linked list separated by a single space.
The second line contains the value of 'i'. It denotes the position in the given singly linked list.

Remember/Consider :
While specifying the list elements for input, 
-1 indicates the end of the singly linked list and hence, would never be a list element.

Output format :
For each test case, print the node data at the 'i-th' position of the linked list(if exists).
Output for every test case will be printed in a seperate line.
"""
Sample Input 1 :
1
3 4 5 2 6 1 9 -1
3
Sample Output 1 :
2

Sample Input 2 :
2
3 4 5 2 6 1 9 -1
0
9 8 4 0 7 8 -1
3
Sample Output 2 :
3
0

Solution :

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def ithNode(head, i):
    count = 0
    current = head
    while count < i and current != None:
        current = current.next
        count = count + 1
    return current

def ll(arr):
    if arr == []:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

from sys import setrecursionlimit

setrecursionlimit(11000)
arr = list(int(i) for i in input().strip().split(' '))
i = int(input())
l = ll(arr[:-1])
node = ithNode(l, i)
if node:
    print(node.data)


#Delete node
"""
You have been given a linked list of integers. 
Your task is to write a function that deletes a node from a given position, 'pos'.\

Note :
Assume that the Indexing for the linked list always starts from 0.
If the position is greater than or equal to the length of the linked list, 
you should return the same linked list without any change.

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. 
Then the test cases follow.
The first line of each test case or query contains the elements of the linked list separated by a single space. 
The second line contains the integer value of 'pos'. 
It denotes the position in the linked list from where the node has to be deleted.

Output format :
For each test case/query, print the resulting linked list of integers in a row, separated by a single space.
Output for every test case will be printed in a seperate line.
"""
Sample Input 1 :
1
3 4 5 2 6 1 9 -1
3
Sample Output 1 :
3 4 5 6 1 9

Sample Input 2 :
2
3 4 5 2 6 1 9 -1
0
10 20 30 40 50 60 -1
7
Sample Output 2 :
4 5 2 6 1 9
10 20 30 40 50 60

Solution :

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteRec(head, i):
    if (i < 0) :
        return head
    if (head == None):
        return None
    if (i == 0) :
        res = head.next
        return res
    head.next = deleteRec(head.next, i-1 )
    return head
    pass

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
i=int(input())
l = deleteRec(l, i)
printll(l)


#Find a Node in Linked List
"""
You have been given a singly linked list of integers. 
Write a function that returns the index/position of an integer data denoted by 'N'(if it exists). -1 otherwise.

Note :
Assume that the Indexing for the singly linked list always starts from 0.

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. 
Then the test cases follow.
The first line of each test case or query contains the elements of the singly linked list separated by a single space. 
The second line contains the integer value 'N'. 
It denotes the data to be searched in the given singly linked list.

Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, 
would never be a list element.

Output format :
For each test case/query, print the index/position of 'N' in the singly linked list. -1, otherwise.
Output for every test case will be printed in a seperate line.
"""
Sample Input 1 :
2
3 4 5 2 6 1 9 -1
5
10 20 30 40 50 60 70 -1
6
Sample Output 1 :
2
-1

Sample Input 2 :
1
3 4 5 2 6 1 9 -1
6
Sample Output 2 :
4
Explanation for Sample Input 2 :
For the given singly linked list, considering the indices starting from 0,
progressing in a left to right manner with a jump of 1, then the N = 6 appears at position 4.

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


#AppendLastNToFirst
"""
You have been given a singly linked list of integers along with an integer 'N'. 
Write a function to append the last 'N' nodes towards the front of the singly linked list and returns the new head to the list.

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. 
Then the test cases follow.
The first line of each test case or query contains the elements of the singly linked list separated by a single space. 
The second line contains the integer value 'N'. It denotes the number of nodes to be moved from last to the front of the singly linked list.

Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element.

Output format :
For each test case/query, print the resulting singly linked list of integers in a row, separated by a single space.
Output for every test case will be printed in a seperate line.
"""
Sample Input 1 :
2
1 2 3 4 5 -1
3
10 20 30 40 50 60 -1
5
Sample Output 1 :
3 4 5 1 2
20 30 40 50 60 10

Sample Input 2 :
1
10 6 77 90 61 67 100  -1
4
Sample Output 2 :
90 61 67 100 10 6 77
Explanation to Sample Input 2 :
We have been required to move the last 4 nodes to the front of the list. Here, "90->61->67->100" is the list which represents the last 4 nodes.
When we move this list to the front then the remaining part of the initial list which is, "10->6->77" is attached after 100. Hence,
the new list formed with an updated head pointing to 90.

Solution :

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    count = 0
    while head is not None:
        head = head.next
        count += 1

    return count

def append_LinkedList(head, n):
    if head == None or head.next == None:
        return head
    curr = head
    temp2 = head
    count = 0
    l = length(head)
    while count < l - n - 1:
        curr = curr.next
        count += 1
    temp1 = curr.next
    head = temp1
    curr.next = None
    while temp1.next != None:
        temp1 = temp1.next
    temp1.next = temp2
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
i = int(input())
l = append_LinkedList(l, i)
printll(l)


#Eliminate duplicates from LL
"""
You have been given a singly linked list of integers where the elements are sorted in ascending order. 
Write a function that removes the consecutive duplicate values such that the given list only contains unique elements and returns the head to the updated list.

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. 
Then the test cases follow.
The first and the only line of each test case or query contains the elements(in ascending order) of the singly linked list separated by a single space.

Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element.

Output format :
For each test case/query, print the resulting singly linked list of integers in a row, separated by a single space.
Output for every test case will be printed in a seperate line.
"""
Sample Input 1 :
1
1 2 3 3 4 3 4 5 4 5 5 7 -1
Sample Output 1 :
1 2 3 4 3 4 5 4 5 7

Sample Input 2 :
2
10 20 30 40 50 -1
10 10 10 10 -1
Sample Output 2 :
10 20 30 40 50
10

Solution :

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def eliminate_duplicate(head):
    temp = head
    if temp is None:
        return
    while temp.next is not None:
        if temp.data == temp.next.data:
            new = temp.next.next
            temp.next = None
            temp.next = new
        else:
            temp = temp.next
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
l = eliminate_duplicate(l)
printll(l)


#Print Reverse LinkedList
"""
You have been given a singly linked list of integers. Write a function to print the list in a reverse order.
To explain it further, you need to start printing the data from the tail and move towards the head of the list, 
printing the head data at the end.

Note :
You can’t change any of the pointers in the linked list, just print it in the reverse order.

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
The first and the only line of each test case or query contains the elements of the singly linked list separated by a single space.

Remember/Constraints :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element.

Output format :
For each test case, print the singly linked list of integers in a reverse fashion, in a row, separated by a single space.
Output for every test case will be printed in a seperate line.
"""
Sample Input 1 :
1
1 2 3 4 5 -1
Sample Output 1 :
5 4 3 2 1

Sample Input 2 :
2
1 2 3 -1
10 20 30 40 50 -1
Sample Output 2 :
3 2 1
50 40 30 20 10

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


#Palindrome LinkedList
"""
You have been given a head to a singly linked list of integers. Write a function check to whether the list given is a 'Palindrome' or not.

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
First and the only line of each test case or query contains the the elements of the singly linked list separated by a single space.

Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element.

Output format :
For each test case, the only line of output that print 'true' if the list is Palindrome or 'false' otherwise.
"""
Sample Input 1 :
1
9 2 3 3 2 9 -1
Sample Output 1 :
true

Sample Input 2 :
2
0 2 3 2 5 -1
-1
Sample Output 2 :
false
true
Explanation for the Sample Input 2 :
For the first query, it is pretty intuitive that the the given list is not a palindrome, hence the output is 'false'.
For the second query, the list is empty. An empty list is always a palindrome , hence the output is 'true'.

Solution :

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def get_prev_node(self, ref_node):
        current = self.head
        while (current and current.next != ref_node):
            current = current.next
        return current

def is_palindrome(llist):
    start = llist.head
    end = llist.last_node
    while (start != end and end.next != start):
        if start.data != end.data:
            return False
        start = start.next
        end = llist.get_prev_node(end)
    return True

a_llist = LinkedList()

data_list = input().split()
for data in data_list:
    if int(data) != -1:
        a_llist.append(int(data))

if is_palindrome(a_llist):
    print('true')
else:
    print('false')
