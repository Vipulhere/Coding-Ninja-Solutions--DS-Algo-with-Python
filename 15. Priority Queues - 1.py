#Code : Remove Min
"""
Implement the function RemoveMin for the min priority queue class.
For a minimum priority queue, write the function for removing the minimum element present.
Remove and return the minimum element.
Note : main function is given for your reference which we are using internally to test the code.
"""

Solution :

class PriorityQueueNode:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.pq = []

    def isEmpty(self):
        return self.getSize() == 0

    def getSize(self):
        return len(self.pq)

    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0].value

    def __percolateUp(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex = (childIndex - 1) // 2

            if self.pq[parentIndex].priority > self.pq[childIndex].priority:
                self.pq[parentIndex], self.pq[childIndex] = self.pq[childIndex], self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break

    def insert(self, ele, priority):
        pqNode = PriorityQueueNode(ele, priority)
        self.pq.append(pqNode)
        self.__percolateUp()

    def __percolatedown(self):

        parenti = 0
        lc = 2 * (parenti) + 1
        rc = 2 * (parenti) + 2
        while lc < self.getSize():
            mi = parenti
            if self.pq[mi].priority > self.pq[lc].priority:
                mi = lc
            if self.getSize() > rc and self.pq[mi].priority > self.pq[rc].priority:
                mi = rc
            if mi == parenti:
                break
            self.pq[parenti], self.pq[mi] = self.pq[mi], self.pq[parenti]
            parenti = mi
            lc = 2 * (parenti) + 1
            rc = 2 * (parenti) + 2

    def removeMin(self):
        if self.isEmpty():
            return None
        rel = self.pq[0].value
        self.pq[0] = self.pq[self.getSize() - 1]
        self.pq.pop()
        self.__percolatedown()
        return rel

myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i = 1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i += 1
        myPq.insert(element, element)
    elif choice == 2:
        print(myPq.getMin())
    elif choice == 3:
        print(myPq.removeMin())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i += 1


#Code : Max Priority Queue
"""
Implement the class for Max Priority Queue which includes following functions -

1. getSize -
Return the size of priority queue i.e. number of elements present in the priority queue.

2. isEmpty -
Check if priority queue is empty or not. Return true or false accordingly.

3. insert -
Given an element, insert that element in the priority queue at the correct position.

4. getMax -
Return the maximum element present in the priority queue without deleting. 
Return -Infinity if priority queue is empty.

5. removeMax -
Delete and return the maximum element present in the priority queue. 
Return -Infinity if priority queue is empty.

Note : main function is given for your reference which we are using internally to test the class.
"""

Solution :

class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.pq = []

    def isEmpty(self):
        return self.getSize() == 0

    def getSize(self):
        return len(self.pq)

    def getMax(self):
        if self.isEmpty() is True:
            return None
        return self.pq[0].value

    def __upHeapify(self):
        child_index = self.getSize() - 1

        while child_index > 0:
            parent_index = (child_index - 1) // 2

            if self.pq[parent_index].priority < self.pq[child_index].priority:
                self.pq[parent_index], self.pq[child_index] = self.pq[child_index], self.pq[parent_index]
                child_index = parent_index
            else:
                break

    def insert(self, ele, priority):
        pqNode = Node(ele, priority)
        self.pq.append(pqNode)
        self.__upHeapify()

    def __downHeapify(self):
        parent_index = 0
        child_left_index = 2 * parent_index + 1
        child_right_index = 2 * parent_index + 2

        while child_left_index < self.getSize():
            max_index = parent_index

            if self.pq[max_index].priority < self.pq[child_left_index].priority:
                max_index = child_left_index
            if child_right_index < self.getSize() and self.pq[max_index].priority < self.pq[child_right_index].priority:
                max_index = child_right_index

            if max_index == parent_index:
                break
            self.pq[parent_index], self.pq[max_index] = self.pq[max_index], self.pq[parent_index]
            parent_index = max_index
            child_left_index = 2 * parent_index + 1
            child_right_index = 2 * parent_index + 2

    def removeMax(self):
        if self.isEmpty() is True:
            return None
        value = self.pq[0].value
        self.pq[0] = self.pq[self.getSize() - 1]
        self.pq.pop()
        self.__downHeapify()
        return value

myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i = 1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i += 1
        myPq.insert(element, element)
    elif choice == 2:
        print(myPq.getMax())
    elif choice == 3:
        print(myPq.removeMax())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i += 1
