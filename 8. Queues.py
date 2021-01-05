#Queue Using LL
"""
You need to implement a Queue class using linked list.
All the required data members should be private.

Implement the following public functions :

1. Constructor -
Initialises the data members.

2. enqueue :
This function should take one argument of type T and has return type void.
This function should insert an element in the queue. Time complexity should be O(1).

3. dequeue :
This function takes no input arguments and has return type T.
This should removes the first element which is entered and return that element as an answer.
Time complexity should be O(1).

4. front :
This function takes no input arguments and has return type T.
This should return the first element which is entered and return that element as an answer.
Time complexity should be O(1).

5. size :
Return the size of stack i.e. count of elements which are present ins stack right now.
Time complexity should be O(1).

6. isEmpty :
Checks if the queue is empty or not. Return true or false.
"""

Solution :

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueUsingLL:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def enqueue(self, data):
        newNode = Node(data)
        if self.__head is None:
            self.__head = newNode
        else:
            self.__tail.next = newNode
        self.__tail = newNode
        self.__count = self.__count + 1

    def dequeue(self):
        if self.__head is None:
            return 0
        data = self.__head.data
        self.__head = self.__head.next
        self.__count = self.__count - 1
        return data

    def front(self):
        if self.__head is None:
            return 0
        data = self.__head.data

        return data

    def isEmpty(self):
        return self.getSize() == 0

    def getSize(self):
        return self.__count

q = QueueUsingLL()
li = [int(ele) for ele in input().split()]
i = 0
while i < len(li):
    choice = li[i]
    if choice == -1:
        break
    elif choice == 1:
        q.enqueue(li[i + 1])
        i += 1
    elif choice == 2:
        ans = q.dequeue()
        if ans != 0:
            print(ans)
        else:
            print(-1)
    elif choice == 3:
        ans = q.front()
        if ans != 0:
            print(ans)
        else:
            print(-1)
    elif choice == 4:
        print(q.getSize())
    elif choice == 5:
        if (q.isEmpty()):
            print('true')
        else:
            print('false')
    i += 1


#Stack Using 2 Queues
"""
You need to implement a Stack class using two queues as its data members.
Only 2 data members should be there inside the class - two queues, 
which should be created dynamically and both should be public. Use the inbuilt queue.

Implement the following public functions :

1. Constructor -
Initialises both the data members.

2. push :
This function should take one argument of type T and has return type void. 
This function should insert an element in the stack. Time complexity should be O(1).

3. pop :
This function takes no input arguments and has return type T. 
This should removes the last element which is entered and return that element as an answer.

4. top :
This function takes no input arguments and has return type T. 
This should return the last element which is entered and return that element as an answer.

5. getSize :
Return the size of stack i.e. count of elements which are present ins stack right now. 
Time complexity should be O(1).
"""

Solution :

import queue

class StackUsingQueues:

    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
        self.curr_size = 0

    def push(self, data):

        self.curr_size += 1
        self.q2.put(data)

        while (not self.q1.empty()):
            self.q2.put(self.q1.queue[0])
            self.q1.get()
        self.q = self.q1
        self.q1 = self.q2
        self.q2 = self.q

    def pop(self):

        if (self.q1.empty()):
            return
        x = self.q1.get()
        self.curr_size -= 1
        return x

    def top(self):
        if (self.q1.empty()):
            return -1
        return self.q1.queue[0]

    def getSize(self):
        return self.curr_size

s = StackUsingQueues()
li = [int(ele) for ele in input().split()]
i = 0
li1 = []
while i < len(li):
    choice = li[i]
    if choice == -1:
        break
    elif choice == 1:
        s.push(li[i + 1])
        i += 1
    elif choice == 2:
        ans = s.pop()
        if ans != 0:
            print(ans)
        else:
            print(-1)
    elif choice == 3:
        ans = s.top()
        if ans != 0:
            print(ans)
        else:
            print(-1)
    elif choice == 4:
        print(s.getSize())
    elif choice == 5:
        while s.q1.qsize() != 0:
            li1.append(s.q1.get())
        li1.reverse()
        print(*li1)

    i += 1


#Reverse Queue
"""
Given a queue of integers, reverse it without help of any explicit stack or queue. 
You need to change in the given queue itself.

Note : No need to return or print the queue.

Input format :
Line 1 : First Element - Size of Queue, Rest Elements - Elements Of Queue

Output format :
Queue elements
"""
Sample Input :
4 1 2 3 4     (1 is at front)
Sample Output :
4 3 2 1    (4 is at front)

Solution :

import queue

def reverseQueue(q1):
    Stack = []
    while (not q1.empty()):
        Stack.append(q1.queue[0])
        q1.get()
    while (len(Stack) != 0):
        q1.put(Stack[-1])
        Stack.pop()

from sys import setrecursionlimit
setrecursionlimit(11000)
li = [int(ele) for ele in (input().split()[1:])]
q1 = queue.Queue()
for ele in li:
    q1.put(ele)
reverseQueue(q1)
while (q1.empty() is False):
    print(q1.get(), end=' ')


#Reverse first K elements
"""
Given a queue and an integer k, reverse first k elements. Return the updated queue.
Do the problem in O(n) complexity.

Input Format :
Line 1 : Integer N, Size of Queue
Line 2 : Queue Elements (separated by space)
Line 3 : Integer k

Output Format:
Updated Queue elements
"""
Sample Input 1:
5
1 2 3 4 5
3
Sample Output 1:
3 2 1 4 5

Sample Input 2:
7
3 4 2 5 6 7 8
7
Sample Output 2:
8 7 6 5 2 4 3

Solution :

import queue

def reverseFirstK(q, k):
    if (q.empty() == True or k > q.qsize()):
        return
    if (k <= 0):
        return
    Stack = []
    for i in range(k):
        Stack.append(q.queue[0])
        q.get()
    while (len(Stack) != 0):
        q.put(Stack[-1])
        Stack.pop()
    for i in range(q.qsize() - k):
        q.put(q.queue[0])
        q.get()

from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
li = [int(ele) for ele in input().split()]
q = queue.Queue()
for ele in li:
    q.put(ele)
k = int(input())
reverseFirstK(q, k)
while (q.qsize() > 0):
    print(q.get())
    n -= 1
