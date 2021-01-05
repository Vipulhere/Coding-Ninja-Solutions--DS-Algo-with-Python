#Geometric Sum
"""
Given k, find the geometric sum i.e.
1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^k)
using recursion.

Input format :
Integer k

Output format :
Geometric sum
"""
Sample Input 1 :
3
Sample Output 1 :
1.875

Sample Input 2 :
4
Sample Output 2 :
1.93750

Solution :

def gsum(s):
    if s==0:
        return 1
    cal=1/(2**s)
    r=gsum(s-1)
    ans=r+cal
    return ans
s=int(input())
x=gsum(s)
print("%.5f" %x)


#Check Palindrome (recursive)
"""
Check whether a given String S is a palindrome using recursion. Return true or false.

Input Format :
String S

Output Format :
'true' or 'false'
"""
Sample Input 1 :
racecar
Sample Output 1:
true

Sample Input 2 :
ninja
Sample Output 2:
false

Solution :

def Palindrome(str):
    size = len(str)
    if size <= 1:
        return True
    if str[0] != str[size-1]:
        return False
    return Palindrome(str[1:-1])

from sys import setrecursionlimit
setrecursionlimit(11000)
str = input()
if Palindrome(str):
    print('true')
else:
    print('false')


#Sum of digits (recursive)
"""
Write a recursive function that returns the sum of the digits of a given integer.

Input format :
Integer N

Output format :
Sum of digits of N
"""
Sample Input 1 :
12345
Sample Output 1 :
15

Sample Input 2 :
9
Sample Output 2 :
9

Solution :

def sumOfDigits(n):
    if n == 0:
        return 0

    smallAns = sumOfDigits(n // 10)
    return smallAns + n % 10

from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
print(sumOfDigits(n))


#Multiplication (Recursive)
"""
Given two integers M & N, calculate and return their multiplication using recursion.
You can only use subtraction and addition for your calculation. No other operators are allowed.

Input format :
Line 1 : Integer M
Line 2 : Integer N

Output format :
M x N
"""
Sample Input 1 :
3
5
Sample Output 1 :
15

Sample Input 2 :
4
0
Sample Output 2 :
0

Solution :

def multiply(m, n):
    if m == 0 or n == 0:
        return 0

    if n > 0:
        smallAns = multiply(m, n - 1)
        return smallAns + m

    else:
        smallAns = multiply(m, n + 1)
        return smallAns - m

from sys import setrecursionlimit
setrecursionlimit(11000)
m = int(input())
n = int(input())
print(multiply(m, n))


#Count Zeros
"""
Given an integer N, count and return the number of zeros that are present in the given integer using recursion.

Input Format :
Integer N

Output Format :
Number of zeros in N
"""
Sample Input 1 :
10204
Sample Output 1 :
2

Sample Input 2 :
708000
Sample Output 2 :
4

Solution :

def countZeros(n):
    if n < 0:
        n *= -1

    if n < 10:
        if n == 0:
            return 1
        return 0

    smallAns = countZeros(n // 10)
    if n % 10 == 0:
        smallAns += 1
    return smallAns

from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
print(countZeros(n))


#String to Integer
"""
Write a recursive function to convert a given string into the number it represents.
That is input will be a numeric string that contains only numbers, 
you need to convert the string into corresponding integer and return the answer.

Input format :
Numeric string S (string, Eg. "1234")

Output format :
Corresponding integer N (int, Eg. 1234)
"""
Sample Input 1 :
1231
Sample Output 1 :
1231

Sample Input 2 :
12567
Sample Output 2 :
12567

Solution :

def string_int(n):
    a=int(n)
    return a

n=input()
r=string_int(n)
print(r)


#Pair star
"""
Given a string S, compute recursively a new string where identical chars 
that are adjacent in the original string are separated from each other by a "*".

Input format :
String S

Output format :
Modified string
"""
Sample Input 1 :
hello
Sample Output 1:
hel*lo

Sample Input 2 :
aaaa
Sample Output 2 :
a*a*a*a

Solution :

def pairStar(Input, Output, i=0):
    Output = Output + Input[i]

    if (i == len(Input) - 1):
        print(Output)
        return;

    if (Input[i] == Input[i + 1]):
        Output = Output + '*';

    pairStar(Input, Output, i + 1);

if __name__ == "__main__":
    Input = input()
    Output = ""
    pairStar(Input, Output);


#Check AB
"""
Suppose you have a string, S, made up of only 'a's and 'b's. 
Write a recursive function that checks if the string was generated using the following rules:

a. The string begins with an 'a'
b. Each 'a' is followed by nothing or an 'a' or "bb"
c. Each "bb" is followed by nothing or an 'a'

If all the rules are followed by the given string, return true otherwise return false.

Input format :
String S

Output format :
'true' or 'false'
"""
Sample Input 1 :
abb
Sample Output 1 :
true

Sample Input 2 :
abababa
Sample Output 2 :
false

Solution :

def checkAB(str):
    if (len(str) == 0):
        return True

    if (str[0] == 'a'):
        if (len(str[1:]) > 1 and str[1:3] == 'bb'):
            return checkAB(str[3:])

        else:
            return checkAB(str[1:])

    else:
        return False

str = input()
if (checkAB(str)):
    print('true')
else:
    print('false')


#Staircase
"""
A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time.
Implement a method to count how many possible ways the child can run up to the stairs.
You need to return number of possible ways W.

Input format :
Integer N

Output Format :
Integer W
"""
Sample Input 1 :
4
Sample Output 1 :
7

Sample Input 2 :
5
Sample Output 2 :
13

Solution :

def staircase(n):
    if (n < 3):
        return n

    if n == 3:
        return 4
    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)

n = int(input())
count = staircase(n)
print(count)
