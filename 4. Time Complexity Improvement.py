#Power Of A Number
"""
Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to return the answer.
Do this recursively.

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

def Power(x, n):
    if n == 0:
        return 1

    smallAns = Power(x, n - 1)

    return smallAns * x

from sys import setrecursionlimit
setrecursionlimit(11000)
x, n = list(int(i) for i in input().strip().split(' '))
print(Power(x, n))


#Array Intersection
"""
Given two random integer arrays, print their intersection.
That is, print all the elements that are present in both the given arrays.
Input arrays can contain duplicate elements.

Note : Order of elements are not important

Input format :
Line 1 : Integer N, Array 1 Size
Line 2 : Array 1 elements (separated by space)
Line 3 : Integer M, Array 2 Size
Line 4 : Array 2 elements (separated by space)

Output format :
Print intersection elements in different lines
"""
Sample Input 1 :
6
2 6 8 5 4 3
4
2 3 4 7
Sample Output 1 :
2
4
3

Sample Input 2 :
4
2 6 1 2
5
1 2 3 4 2
Sample Output 2 :
2
2
1

Solution :

def intersection(arr1, arr2):
    arr1.sort()
    arr2.sort()
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            print(arr1[i])
            i += 1
            j += 1

n1 = int(input())
arr1 = list(int(i) for i in input().strip().split(' '))
n2 = int(input())
arr2 = list(int(i) for i in input().strip().split(' '))
intersection(arr1, arr2)


#Array Equilibrium Index
"""
Find and return the equilibrium index of an array. 
Equilibrium index of an array is an index i such that,
the sum of elements at indices less than i is equal to the sum of elements at indices greater than i.
Element at index i is not included in either part.
If more than one equilibrium index is present, you need to return the first one. 
And return -1 if no equilibrium index is present.

Input format :
Line 1 : Size of input array
Line 2 : Array elements (separated by space)
"""
Sample Input :
7
-7 1 5 2 -4 3 0
Sample Output :
3

Solution :

def equilibrium(arr):
    total_sum = sum(arr)
    leftsum = 0
    for i, num in enumerate(arr):

        total_sum -= num

        if leftsum == total_sum:
            return i
        leftsum += num

    return -1

n1 = int(input())
arr = list(int(i) for i in input().strip().split(' '))
print(equilibrium(arr))


#Find the Unique Element
"""
Given an integer array of size 2N + 1. In this given array, 
N numbers are present twice and one number is present only once in the array.
You need to find and return that number which is unique in the array.

Note : Given array will always contain odd number of elements.

Input format :
Line 1 : Array size i.e. 2N+1
Line 2 : Array elements (separated by space)

Output Format :
Unique element present in the array
"""
Sample Input :
7
2 3 1 6 3 6 2
Sample Output :
1

Solution :

def find_unique(li):
    ele = li[0]
    for i in range(1, len(li)):
        ele = ele ^ li[i]
    return ele

n = int(input())
li = [int(x) for x in input().split()]
unique = find_unique(li)
print(unique)


#Duplicate in array
"""
Given an array of integers of size n which contains numbers from 0 to n - 2. 
Each number is present at least once. That is, if n = 5, 
numbers from 0 to 3 is present in the given array at least once and one number is present twice. 
You need to find and return that duplicate number present in the array.
Assume, duplicate number is always present in the array.

Input format :
Line 1 : Size of input array
Line 2 : Array elements (separated by space)

Output Format :
Duplicate element
"""
Sample Input:
9
0 7 2 5 4 7 1 3 6
Sample Output:
7

Solution :

def DuplicateNumber(arr):
    n = len(arr) - 2
    totalSum = 0

    for i in arr:
        totalSum += i

    #sum of n natural numbers
    sum = int(n*(n+1)/2)
    return totalSum - sum

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
ans=DuplicateNumber(arr)
print(ans)


#Pair sum in array
"""
Given a random integer array A and a number x. 
Find and print the pair of elements in the array which sum to x.
Array A can contain duplicate elements.
While printing a pair, print the smaller element first.
That is, if a valid pair is (6, 5) print "5 6". 
There is no constraint that out of 5 pairs which have to be printed in 1st line. 
You can print pairs in any order, just be careful about the order of elements in a pair.

Input format :
Line 1 : Integer N (Array size)
Line 2 : Array elements (separated by space)
Line 3 : Integer x

Output format :
Line 1 : Pair 1 elements (separated by space)
Line 2 : Pair 2 elements (separated by space)
Line 3 : and so on
"""
Sample Input:
9
1 3 6 2 5 4 3 2 4
7
Sample Output :
1 6
3 4
3 4
2 5
2 5
3 4
3 4

Solution :
n = int(input())
a = [int(x) for x in input().split()]
sum = int(input())

for i in range (len(a)):
    for j in range (i+1,len(a)):
        if a[i]+a[j]==sum:

            if(a[i]<a[j]):
                print(a[i]," ",a[j])

            else:
                print(a[j]," ",a[i])


#Triplet sum
"""
Given a random integer array and a number x. 
Find and print the triplets of elements in the array which sum to x.
While printing a triplet, print the smallest element first.
That is, if a valid triplet is (6, 5, 10) print "5 6 10". 
There is no constraint that out of 5 triplets which have to be printed on 1st line. 
You can print triplets in any order, just be careful about the order of elements in a triplet.

Input format :
Line 1 : Integer N (Array Size)
Line 2 : Array elements (separated by space)
Line 3 : Integer x

Output format :
Line 1 : Triplet 1 elements (separated by space)
Line 2 : Triplet 3 elements (separated by space)
Line 3 : and so on
"""
Sample Input:
7
1 2 3 4 5 6 7
12
Sample Output ;
1 4 7
1 5 6
2 3 7
2 4 6
3 4 5

Solution :

def count(arr, x):
    counter = 0
    for i in arr:

        if i == x:
            counter += 1

    return counter

def tripletSum(arr, x):
    arr.sort()

    for k in range(len(arr) - 2):
        i, j = k + 1, len(arr) - 1
        while j > i:

            if arr[i] + arr[j] + arr[k] == x:
                dup_j = count(arr[i + 1:], arr[j])

                for z in range(dup_j):
                    print(arr[k], arr[i], arr[j])

                i += 1

            elif arr[i] + arr[j] + arr[k] > x:
                j -= 1

            elif arr[i] + arr[j] + arr[k] < x:
                i += 1

n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
sum = int(input())
tripletSum(arr, sum)


#Rotate array
"""
You have been given a random integer array/list(ARR) of size N. 
Write a function that rotates the given array/list by D elements(towards the left).

Note:
Change in the input array/list itself. You don't need to return or print the elements.

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. 
Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the array/list.

Second line contains 'N' single space separated integers representing the elements in the array/list.

Third line contains the value of 'D' by which the array/list needs to be rotated.

Output Format :
For each test case, print the rotated array/list in a row separated by a single space.
Output for every test case will be printed in a separate line.
"""
Sample Input 1:
1
7
1 2 3 4 5 6 7
2
Sample Output 1:
3 4 5 6 7 1 2

Sample Input 2:
2
7
1 2 3 4 5 6 7
0
4
1 2 3 4
2
Sample Output 2:
1 2 3 4 5 6 7
3 4 1 2

Solution :

def leftRotate(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr, n)

def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp

def printArray(arr, size):
    for i in range(size):
        print("%d" % arr[i], end=" ")

n = int(input())
arr = [int(x) for x in input().split()]
d = int(input())
leftRotate(arr, d, n)
printArray(arr, n)
