#Code : Stack Using LL
"""
You need to implement a Stack class using linked list.
The data members should be private.
Implement the following public functions :

1. Constructor -
Initialises the data member (i.e. head to null).

2. push :
This function should take one argument of type T and has return type void.
This function should insert an element in the stack. Time complexity should be O(1).

3. pop :
This function takes no input arguments and has return type T.
This should removes the last element which is entered and return that element as an answer.
Time complexity should be O(1).

4. top :
This function takes no input arguments and has return type T.
This should return the last element which is entered and return that element as an answer.
Time complexity should be O(1).

5. size :
Return the size of stack i.e. count of elements which are present ins stack right now.
Time complexity should be O(1).

6. isEmpty :
Checks if the stack is empty or not. Return true or false.
"""
Solution :

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackUsingLL:

    def __init__(self):
        self.__head = None
        self.__size = 0

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.__head
        self.__head = newNode
        self.__size = self.__size + 1

    def pop(self):
        if self.isEmpty() is True:
            return 0
        data = self.__head.data
        self.__head = self.__head.next
        self.__size = self.__size - 1
        return data

    # Return 0 if stack is empty. Don't display any other message

    def top(self):
        if self.isEmpty() is True:
            return 0
        data = self.__head.data
        return data

    # Return 0 if stack is empty. Don't display any other message

    def isEmpty(self):
        return self.getSize() == 0

    def getSize(self):
        return self.__size

li = [int(ele) for ele in input().split()]
s = StackUsingLL()
i = 0
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
        if (s.isEmpty()):
            print('true')
        else:
            print('false')
    i += 1


#Balanced Paranthesis
"""
Given a string expression, check if brackets present in the expression are balanced or not. 
Brackets are balanced if the bracket which opens last, closes first.
You need to return true if it is balanced, false otherwise.

Note: This problem was asked in initial rounds in Facebook
"""
Sample Input 1 :
{ a + [ b+ (c + d)] + (e + f) }
Sample Output 1 :
true

Sample Input 2 :
{ a + [ b - c } ]
Sample Output 2 :
false

Solution :

def checkBalanced(expr):
    s=[]
    for char in expr:
        if char in '({[':
            s.append(char)
        elif char is ')':
            if(not s or s[-1]!='('):
                return False
            s.pop()
        elif char is '}':
            if(not s or s[-1]!='{'):
                return False
            s.pop()
        elif char is ']':
            if(not s or s[-1]!='['):
                return False
            s.pop()
    if (not s):
        return True
    return False

exp=input()
if checkBalanced(exp):
    print('true')
else:
    print('false')


#Reverse Stack
"""
Reverse a given Stack with the help of another empty stack. Two stacks will be given. 
Out of which first contains some integers and second one is empty. 
You need to reverse the first one using second stack. Change in the given first stack itself.

Note : You don't need to print or return the stack, 
just reverse the given stack and it will be printed internally.

Input format :
Line 1 : Size of Stack
Line 2 : Stack elements (separated by space)
"""
Sample Input :
4
1 2 3 4     (4 is at top)
Sample Output :
1 2 3 4    (1 is at top)

Solution :

def reverseStack(s1, s2):
    if (len(s1) <= 1):
        return
    while (len(s1) != 1):
        ele = s1.pop()
        s2.append(ele)
    lastEle = s1.pop()
    while (len(s2) != 0):
        ele = s2.pop()
        s1.append(ele)
    reverseStack(s1, s2)
    s1.append(lastEle)

from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
s1 = [int(ele) for ele in input().split()]
s2 = []
reverseStack(s1, s2)
while (len(s1) != 0):
    print(s1.pop(), end=' ')


#Check redundant brackets
"""
Given a string mathematical expression, return true if redundant brackets are present in the expression. 
Brackets are redundant if there is nothing inside the bracket or more than one pair of brackets are present.
Assume the given string expression is balanced and contains only one type of bracket i.e. ().

Note: You will not get partial score for this problem. You will get marks only if all test cases are passed.

Input Format :
String s (Expression)

Output Format :
true or false
"""
Sample Input 1:
((a + b))
Sample Output 1:
true

Sample Input 2:
(a+b)
Sample Output 2:
false

Solution :

def checkRedundancy(Str):
    st = []
    for ch in Str:
        if (ch == ')'):
            top = st[-1]
            st.pop()
            flag = True
            while (top != '('):
                if (top == '+' or top == '-' or top == '*' or top == '/'):
                    flag = False
                top = st[-1]
                st.pop()
            if (flag == True):
                return True
        else:
            st.append(ch)
    return False
def findRedundant(Str):
    ans = checkRedundancy(Str)
    if (ans == True):
        print("true")
    else:
        print("false")
if __name__ == '__main__':
    Str =input()
    findRedundant(Str)


#Stock Span
"""
The span si of a stock’s price on a certain day i is the minimum number of consecutive days (up to the current day) the price of the stock has been less than its price on that ith day. 
If for a particular day, if no stock price is greater then just count the number of days till 0th day including current day.
For eg. if given price array is {3, 6, 8, 1, 2}, span for 4th day (which has price 2) is 2 because minimum count of consecutive days (including 4th day itself) from current day which has price less than 4th day is 2 (i.e. day 3 & 4). 
Similarly, span for 2nd day is 3 because no stock price in left is greater than 2nd day's price. So count is 3 till 0th day.
Given an input array with all stock prices, you need to return the array with corresponding spans of each day.

Note : Try doing it in O(n).

Input format :
Line 1 : Integer n, Arrays Size
Line 2 : Price for n days (separated by space). It can contain duplicate values`

Output format :
Return an array that contain span for each day
"""
Sample Input 1 :
8
60 70 80 100 90 75 80 120
Sample Output 1 :
1 2 3 4 1 1 2 8

Sample Input 2 :
 4
 1 1 1 1
Sample Output 2 :
1 1 1 1

Solution :

def stockSpan(price, n):
    span = []
    span.append(1)
    st = []
    st.append(0)

    for i in range(1, n):
        while len(st) > 0 and price[st[-1]] < price[i]:
            st.pop()
        if len(st) <= 0:
            span.append(i + 1)
        else:
            span.append(i - st[-1])
        st.append(i)

    return span

n = int(input())
price = [int(x) for x in input().split()]
spans = stockSpan(price, n)
for ele in spans:
    print(ele, end=' ')


#Minimum bracket Reversal
"""
Given a string expression which consists only ‘}’ and ‘{‘. The expression may not be balanced. 
You need to find the minimum number of bracket reversals which are required to make the expression balanced.
Return -1 if the given expression can't be balanced.

Input Format :
String S

Output Format :
Required count
"""
Sample Input 1 :
{{{
Sample Output 1 :
-1

Sample Input 2 :
{{{{}}
Sample Output 2 :
1

Solution :

def countBracketReversals(string):
    if(len(string) == 0):
        return 0

    if(len(string)%2 != 0):
        return -1

    s = []
    for char in string:

        if char == '{':
            s.append(char)

        else:
            if(len(s) > 0 and s[-1] == '{'):
                s.pop()

            else:
                s.append(char)
    count = 0

    while(len(s) != 0):
        c1 = s.pop()
        c2 = s.pop()

        if c1!=c2:
            count+=2

        else:
            count+=1

    return count

string = input()
ans = countBracketReversals(string)
print(ans)
