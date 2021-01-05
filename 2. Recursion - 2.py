#Remove X
"""
Given a string, compute recursively a new string where all 'x' chars have been removed.

Input format :
String S

Output format :
Modified String
"""
Sample Input 1 :
xaxb
Sample Output 1:
ab

Sample Input 2 :
abc
Sample Output 2:
abc

Sample Input 3 :
xx
Sample Output 3:

Solution :

def removeX(s,x):
    if len(s)==0:
        return s

    smallOutput=removeX(s[1:],x)

    if s[0]==x:
        return smallOutput

    else:
        return s[0]+smallOutput

s=input()
r=removeX(s,'x')
print(r)


#Remove Duplicates Recursively
"""
Given a string S, remove consecutive duplicates from it recursively.

Input Format :
String S

Output Format :
Output string
"""
Sample Input 1 :
aabccba
Sample Output 1 :
abcba

Sample Input 2 :
xxxyyyzwwzzz
Sample Output 2 :
xyzwz

Solution :

def removeDuplicate(s):

    if len(s)==0 or len(s)==1:
        return s

    if s[0]==s[1]:
        smallOutput=removeDuplicate(s[1:])
        return smallOutput

    else:
        smallOutput=removeDuplicate(s[1:])
        return s[0]+smallOutput

s=input()
r=removeDuplicate(s)
print(r)


#Merge Sort
"""
Sort an array A using Merge Sort.
Change in the input array itself. So no need to return or print anything.

Input format :
Line 1 : Integer n i.e. Array size
Line 2 : Array elements (separated by space)

Output format :
Array elements in increasing order (separated by space)
"""
Sample Input 1 :
6
2 6 8 5 4 3
Sample Output 1 :
2 3 4 5 6 8

Sample Input 2 :
5
2 1 5 2 3
Sample Output 2 :
1 2 2 3 5

Solution :

def mergeSort(arr, start, end):
    size = end - start
    if size <= 1:
        return
    mid = (start + end) // 2
    mergeSort(arr, start, mid)
    mergeSort(arr, mid, end)

    # Merge Two Sorted Lists
    result = [0] * size
    i = start
    j = mid
    k = 0
    while (i < mid and j < end):
        if (arr[i] < arr[j]):
            result[k] = arr[i]
            k += 1
            i += 1
        else:
            result[k] = arr[j]
            k += 1
            j += 1
    while (i < mid):
        result[k] = arr[i]
        k += 1
        i += 1
    while (j < end):
        result[k] = arr[j]
        k += 1
        j += 1
    for i in range(0, size):
        arr[start + i] = result[i]


n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
mergeSort(arr, 0, n)
for num in arr:
    print(num, end=" ")
print()


#Quick Sort
"""
Sort an array A using Quick Sort.
Change in the input array itself. So no need to return or print anything.

Input format :
Line 1 : Integer n i.e. Array size
Line 2 : Array elements (separated by space)

Output format :
Array elements in increasing order (separated by space)
"""
Sample Input 1 :
6
2 6 8 5 4 3
Sample Output 1 :
2 3 4 5 6 8

Sample Input 2 :
5
1 5 2 7 3
Sample Output 2 :
1 2 3 5 7

Solution :

def partition(a,si,ei):
    pivot=a[si]
    c=0
    for i in range(si,ei+1):
        if a[i] < pivot:
            c=c+1
    a[si+c],a[si]=a[si],a[si+c]
    pivot_index=si+c
    i=si
    j=ei
    while i < j :
        if (a[i]<pivot):
            i=i+1
        elif a[j] >= pivot:
            j=j-1
        else:
            a[i],a[j]=a[j],a[i]
            i = i + 1
            j = j - 1
    return pivot_index

def quick_sort(a,si,ei):
    if si>=ei:
        return
    pivot_index=partition(a,si,ei)
    quick_sort(a,si,pivot_index-1)
    quick_sort(a,pivot_index+1,ei)

n=int(input())
a=list(int(i) for i in input().strip().split(' '))
quick_sort(a,0,len(a)-1)
for x in a:
    print(x,end=" ")


#Tower Of Hanoi
"""
Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. 
The objective of the puzzle is to move all disks from source rod to destination rod using third rod (say auxiliary). 
The rules are :
1) Only one disk can be moved at a time.
2) A disk can be moved only if it is on the top of a rod.
3) No disk can be placed on the top of a smaller disk.
Print the steps required to move n disks from source rod to destination rod.
Source Rod is named as 'a', auxiliary rod as 'b' and destination rod as 'c'.

Input Format :
Integer n

Output Format :
Steps in different lines (in one line print source and destination rod name separated by space)
"""
Sample Input 1 :
2
Sample Output 1 :
a b
a c
b c

Sample Input 2 :
3
Sample Output 2 :
a c
a b
c b
a c
b a
b c
a c

Solution :

def tower(n,a,b,c):

    if n==0:
        return

    if n==1:
        print(a,c )
        return

    tower(n-1,a,c,b)

    print(a,c)

    tower(n-1,b,a,c)

n=int(input())
tower(n,"a","b","c")
