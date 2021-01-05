#Maximum Frequency
"""
You are given an array of integers that contain numbers in random order.
Write a program to find and return the number which occurs the maximum times in the given input.
If two or more elements contend for the maximum frequency, return the element which occurs in the array first.

Input Format :
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces

Output Format :
Most frequent element
"""
Sample Input 1 :
13
2 12 2 11 12 2 1 2 2 11 12 2 6
Sample Output 1 :
2
Sample Input 2 :
3
1 4 5
Sample Output 2 :
1

Solution :

def maxFreq(l):
    dict = {}
    count, itm = 0, ''
    for item in reversed(l):
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count :
            count, itm = dict[item], item
    return(itm)

n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(maxFreq(l))


#Pair Sum To 0
"""
Given a random integer array A of size N. Find and print the pair of elements in the array which sum to 0.
Array A can contain duplicate elements.
While printing a pair, print the smaller element first.
That is, if a valid pair is (6, -6) print "-6 6". 
There is no constraint that out of 5 pairs which have to be printed in 1st line. 
You can print pairs in any order, just be careful about the order of elements in a pair.

Input format :
Line 1 : Integer N (Array size)
Line 2 : Array elements (separated by space)

Output format :
Line 1 : Pair 1 elements (separated by space)
Line 2 : Pair 2 elements (separated by space)
Line 3 : and so on
"""
Sample Input:
5
2 1 -2 2 3
Sample Output :
-2 2
-2 2

Solution :

def pairSum0(l):
    dic={}
    k=0
    for num in l:
        if k-num in dic:
            for i in range(dic[k-num]):
                if k-num<num:
                    print(k-num,num)
                else:
                    print(num,k-num)
        if num in dic:
            dic[num]+=1
        else:
            dic[num]=1

n=int(input())
l=list(int(i) for i in input().strip().split(' '))
pairSum0(l)


#Extract Unique characters
"""
Given a string, you need to remove all the duplicates. 
That means, the output string should contain each character only once. 
The respective order of characters should remain same.

Input format :
String S

Output format :
Output String
"""
Sample Input 1 :
ababacd
Sample Output 1 :
abcd
Sample Input 2 :
abcde
Sample Output 2 :
abcde

Solution :

from collections import OrderedDict

def removeDupWithOrder(str):
    return "".join(OrderedDict.fromkeys(str))

if __name__ == "__main__":
    str = input()
    print(removeDupWithOrder(str))


#Longest consecutive Sequence
"""
You are given with an array of integers that contain numbers in random order. 
Write a program to find the longest possible sequence of consecutive numbers using the numbers from given array.
You need to return the output array which contains consecutive elements. 
Order of elements in the output is not important.
Best solution takes O(n) time.
If two sequences are of equal length then, 
return the sequence starting with the number whose occurrence is earlier in the array.

Input Format :
Line 1 : Integer n, Size of array
Line 2 : Array elements (separated by space)
"""
Sample Input 1 :
13
2 12 9 16 10 5 3 20 25 11 1 8 6
Sample Output 1 :
8
9
10
11
12
Sample Input 2 :
7
3 7 2 1 9 8 1
Sample Output 2 :
7
8
9
Explanation: Sequence should be of consecutive numbers. Here we have 2 sequences with same length i.e. [1, 2, 3] and [7, 8, 9], but output should be [7, 8, 9] because the starting point of [7, 8, 9] comes first in input array.
Sample Input 3 :
7
15 24 23 12 19 11 16
Sample Output 3 :
15
16

Solution :

def longestConsecutiveSubsequence(l):
    m = {l[i]:i for i in range(len(l)-1,-1,-1)}
    visited = {}
    start,end = l[0],l[0]
    startM,endM = start,end
    for num in l:
        if num not in visited:
            visited[num] = True
            start,end = num,num
            while start-1 in m:
                start-=1
                visited[start] = True
            while end+1 in m:
                end+=1
                visited[end] = True
            if (endM-startM+1<end-start+1) or ((endM-startM+1 == end-start+1) and (m[start]<m[startM])):
                startM,endM = start,end
    return startM,endM

n=int(input())
l=list(int(i) for i in input().strip().split(' '))
start,end = longestConsecutiveSubsequence(l)
for num in range(start,end+1):
    print(num)


#Pairs with difference K
"""
You are given with an array of integers and an integer K. 
Write a program to find and print all pairs which have difference K.
Take difference as absolute.

Input Format :
Line 1 : Integer n, Size of array
Line 2 : Array elements (separated by space)
Line 3 : K

Output format :
Print pairs in different lines (pair elements separated by space). In a pair, smaller element should be printed first.
(Order of different pairs is not important)
"""
Sample Input 1 :
4
5 1 2 4
3
Sample Output 1 :
2 5
1 4
Sample Input 2 :
4
4 4 4 4
0
Sample Output 2 :
4 4
4 4
4 4
4 4
4 4
4 4

Solution :

def printSeq(li, k, d):
    if k != 0:
        for ele in li:
            search1 = ele - k
            search2 = k + ele
            if search1 in d:
                for i in range(d[search1] * d[ele]):
                    if search1 < ele:
                        print(search1, ele)
                    else:
                        print(ele, search1)

            if search2 in d:
                for i in range(d[search2] * d[ele]):
                    if search2 > ele:
                        print(ele, search2)
                    else:
                        print(search2, ele)
            d[ele] = 0

    else:
        for i in range(len(li)):
            for j in range(i + 1, len(li)):
                if abs(li[i] - li[j]) == k:
                    if li[i] > li[j]:
                        print(li[j], li[i])
                    else:
                        print(li[i], li[j])

n = int(input())
li = [int(ele) for ele in input().split()]
k = int(input())
d = {}
for ele in li:
    d[ele] = d.get(ele, 0) + 1
printSeq(li, k, d)


#Longest subset zero sum
"""
Given an array consisting of positive and negative integers, 
find the length of the longest subarray whose sum is zero.

NOTE: You have to return the length of longest subarray .

Input Format :
Line 1 : Contains an integer N i.e. size of array
Line 2 : Contains N elements of the array, separated by spaces

Output Format
Line 1 : Length of longest subarray 
"""
Sample Input :
10
 95 -97 -387 -435 -5 -70 897 127 23 284
Sample Output :
5

Solution :

def maxLen(arr):
    hash_map = {}
    max_len = 0
    curr_sum = 0

    for i in range(len(arr)):
        curr_sum += arr[i]
        if arr[i] is 0 and max_len is 0:
            max_len = 1

        if curr_sum is 0:
            max_len = i + 1

        if curr_sum in hash_map:
            max_len = max(max_len, i - hash_map[curr_sum])
        else:

            hash_map[curr_sum] = i

    return max_len

n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
print(maxLen(arr))
