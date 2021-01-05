#Power Of A Number
"""
Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to print the answer.
Note : For this question, you can assume that 0 raised to the power of 0 is 1

Input format :
Two integers x and n (separated by space)

Output Format :
x^n (i.e. x raise to the power n)
"""
Sample Input 1 :
 3 4
Sample Output 1 :
81

Sample Input 2 :
 2 5
Sample Output 2 :
32

Solution :

def Power_Number(X,N):
    output=X**N
    return output

str=input().split()
x,n=int(str[0]),int(str[1])
r=Power_Number(x,n)
print(r)


#Sum Of Array
"""
Given an array of length N, you need to find and return the sum of all elements of the array.
Do this recursively.

Input Format :
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces

Output Format :
Sum
"""
Sample Input 1 :
3
9 8 9
Sample Output 1 :
26

Sample Input 2 :
3
4 2 1
Sample Output 2 :
7

Solution :

n=int(input())
li=[int(x) for x in input().split()]
sum = 0
for list_ele in li:
    sum=sum+list_ele
print(sum)


#Check Number in Array
"""
Given an array of length N and an integer x, you need to find if x is present in the array or not. Return true or false.
Do this recursively.

Input Format :
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces
Line 3 : Integer x

Output Format :
'true' or 'false'
"""
Sample Input 1 :
3
9 8 10
8
Sample Output 1 :
true

Sample Input 2 :
3
9 8 10
2
Sample Output 2 :
false

Solution :

def NumberinArray(li):
    if x in li:
        print("true")
    else:
        print("false")

from sys import setrecursionlimit

setrecursionlimit(11000)
n = int(input())
li = [int(x) for x in input().split()]
x = int(input())
NumberinArray(li)


#First Index of Number - Question
"""
Given an array of length N and an integer x, you need to find and return the first index of integer x present in the array. Return -1 if it is not present in the array.
First index means, the index of first occurrence of x in the input array.
Do this recursively. Indexing in the array starts from 0.

Input Format :
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces
Line 3 : Integer x

Output Format :
first index or -1
"""
Sample Input :
4
9 8 10 8
8
Sample Output :
1

Solution :

def FirstIndex(a,x):
    l=len(a)
    if l==0:
        return -1
    if a[0]==x:
        return 0
    smallerList=a[1:]
    smallerListOutput=FirstIndex(smallerList,x)
    if smallerListOutput==-1:
        return -1
    else:
        return smallerListOutput+1

from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
a=list(int(i) for i in input().strip().split(' '))
x=int(input())
r=FirstIndex(a,x)
print(r)


#Last Index Of Number Question
"""
Given an array of length N and an integer x, you need to find and return the last index of integer x present in the array. Return -1 if it is not present in the array.
Last index means - if x is present multiple times in the array, return the index at which x comes last in the array.
You should start traversing your array from 0, not from (N - 1).
Do this recursively. Indexing in the array starts from 0.

Input Format :
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces
Line 3 : Integer x

Output Format :
last index or -1
"""
Sample Input :
4
9 8 10 8
8
Sample Output :
3

Solution :

def LastIndex(a,x):
    l=len(a)
    if l==0:
        return -1
    smallerList=a[1:]
    smallerListOutput=LastIndex(smallerList,x)
    if smallerListOutput!= -1:
        return smallerListOutput+1
    else:
        if a[0]==x:
            return 0
        else:
            return -1

from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
a=list(int(i) for i in input().strip().split(' '))
x=int(input())
r=LastIndex(a,x)
print(r)
