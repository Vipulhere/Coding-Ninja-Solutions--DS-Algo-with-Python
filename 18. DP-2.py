#Min Cost Path Problem
"""
Given an integer matrix of size m*n,
you need to find out the value of minimum cost to reach from the cell (0, 0) to (m-1, n-1).
From a cell (i, j), you can move in three directions : (i+1, j), (i, j+1) and (i+1, j+1).
Cost of a path is defined as the sum of values of each cell through which path passes.

Input Format :
Line 1 : Two integers, m and n
Next m lines : n integers of each row (separated by space)

Output Format :
Minimum cost
"""
Sample Input :
3 4
3 4 1 2
2 1 8 9
4 7 8 1
Sample Output :
13

Solution :

import sys

def minCost(cost,m,n):
    dp=[[sys.maxsize for i in range(n+1)] for j in range(m+1)]
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if i==m-1 and j== n-1:
                dp[i][j] = cost[i][j]
            else:
                ans1=dp[i+1][j]
                ans2=dp[i][j+1]
                ans3=dp[i+1][j+1]
                dp[i][j] = cost[i][j] + min (ans1, ans2, ans3)
    return dp[0][0]

m,n=[int(i) for i in input().split()]
cost=[[int(j) for j in input().split()] for i in range(m)]
print(minCost(cost,m,n))


#LCS - Problem
"""
Given 2 strings of S1 and S2 with lengths m and n respectively, find the length of longest common subsequence.
A subsequence of a string S whose length is n, 
is a string containing characters in same relative order as they are present in S, 
but not necessarily contiguous. Subsequences contain all the strings of length varying from 0 to n. 
E.g. subsequences of string "abc" are - "",a,b,c,ab,bc,ac,abc.

Input Format :
Line 1 : String S1
Line 2 : String s2

Output Format :
Line 1 : Length of lcs
"""
Sample Input :
adebc
dcadb
Sample Output :
3

Solution :

def lcs(S1 , S2):
    m = len(S1)
    n = len(S2)
    L = [[None]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif S1[i-1] == S2[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])

    return L[m][n]

S1 = input().strip()
S2 = input().strip()
print(lcs(S1, S2))


#0 1 Knapsack - Problem
"""
A thief robbing a store and can carry a maximal weight of W into his knapsack. 
There are N items and ith item weigh wi and is value vi. What is the maximum value V, that thief can take ?

Input Format :
Line 1 : N i.e. number of items
Line 2 : N Integers i.e. weights of items separated by space
Line 3 : N Integers i.e. values of items separated by space
Line 4 : Integer W i.e. maximum weight thief can carry

Output Format :
Line 1 : Maximum value V
"""
Sample Input :
4
1 2 4 5
5 4 8 6
5
Sample Output :
13

Solution :

def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]

N = int(input())
wt = list(int(i) for i in input().strip().split(' '))
val = list(int(i) for i in input().strip().split(' '))
W = int(input())
n = len(val)
print(knapSack(W, wt, val, n))


#Matrix Chain Multiplication
"""
Given a chain of matrices A1, A2, A3,.....An, you have to figure out the most efficient way to multiply these matrices 
i.e. determine where to place parentheses to minimise the number of multiplications.
You will be given an array p[] of size n + 1. Dimension of matrix Ai is p[i - 1]*p[i]. 
You need to find minimum number of multiplications needed to multiply the chain.

Input Format :
Line 1 : Integer n i.e. number of matrices
Line 2 : n + 1 integers i.e. elements of array p[] 

Output Format :
Line 1 : Minimum number of multiplication needed
"""
Sample Input :
3
10 15 20 25
Sample Output :
8000
Sample Output Explanation :
There are two ways to multiply the chain - A1*(A2*A3) or (A1*A2)*A3.
If multiply in order A1*(A2*A3) then number of multiplications required are 15000.
If multiply in order (A1*A2)*A3 then number of multiplications required are 8000.
Thus minimum number of multiplications required are 8000

Solution :

import sys

def MatrixChainOrder(p, n):
    m = [[0 for x in range(n)] for x in range(n)]
    for i in range(1, n):
        m[i][i] = 0
    for L in range(2, n):
        for i in range(1, n-L+1):
            j = i+L-1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
    return m[1][n-1]

N=int(input())
arr =[int(x) for x in input().split()]
size = len(arr)
print(str(MatrixChainOrder(arr, size)))
