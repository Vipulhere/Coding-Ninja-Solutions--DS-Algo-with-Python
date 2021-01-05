#N-Queens
"""
You are given N, and for a given N x N chessboard, find a way to place N queens such that no queen can attack any other queen on the chess board.
A queen can be killed when it lies in the same row, or same column, or the same diagonal of any of the other queens.
You have to print all such configurations.

Input Format :
Line 1 : Integer N

Output Format :
One Line for every board configuration.
Every line will have N*N board elements printed row wise and are separated by space

Note : Don't print anything if there isn't any valid configuration.
"""
Sample Input :
4
Sample Output :
0 1 0 0 0 0 0 1 1 0 0 0 0 0 1 0
0 0 1 0 1 0 0 0 0 0 0 1 0 1 0 0

Solution :

def isSafe(row,col,board,n):
    i= row-1
    while i >= 0:
        if board[i][col]==1:
            return False
        i-=1
    i=row-1
    j=col-1
    while i >=0 and j>=0:
        if board[i][j]==1:
            return False
        i-=1
        j-=1
    i=row-1
    j=col+1
    while i >=0 and j<n:
        if board[i][j]==1:
            return False
        i-=1
        j+=1
    return True

def printPathsHelper(row,n,board):
    if row==n:
        for i in range(n):
            for j in range(n):
                print(board[i][j],end=" ")
        print()
        return
    for col in range(n):
        if isSafe(row,col,board,n) is True:
            board[row][col]=1
            printPathsHelper(row+1,n,board)
            board[row][col]=0
    return

def printPaths(n):
    board=[[0 for j in range(n)] for i in range(n)]
    printPathsHelper(0,n,board)

n= int(input())
printPaths(n)


#Sudoku Solver
"""
Given a 9*9 sudoku board, in which some entries are filled and others are 0 (0 indicates that the cell is empty), 
you need to find out whether the Sudoku puzzle can be solved or not i.e. return true or false.

Input Format :
9 Lines where ith line contains ith row elements separated by space

Output Format :
true or false
"""
Sample Input :
9 0 0 0 2 0 7 5 0
6 0 0 0 5 0 0 4 0
0 2 0 4 0 0 0 1 0
2 0 8 0 0 0 0 0 0
0 7 0 5 0 9 0 6 0
0 0 0 0 0 0 4 0 1
0 1 0 0 0 5 0 8 0
0 9 0 0 7 0 0 0 4
0 8 2 0 4 0 0 0 6
Sample Output :
true

Solution :

def print_grid(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j])
        print('n')

def find_empty_location(arr, l):
    for row in range(9):
        for col in range(9):
            if (arr[row][col] == 0):
                l[0] = row
                l[1] = col
                return True
    return False

def used_in_row(arr, row, num):
    for i in range(9):
        if (arr[row][i] == num):
            return True
    return False

def used_in_col(arr, col, num):
    for i in range(9):
        if (arr[i][col] == num):
            return True
    return False

def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if (arr[i + row][j + col] == num):
                return True
    return False

def check_location_is_safe(arr, row, col, num):
    return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and not used_in_box(arr, row - row % 3,
                                                                                                 col - col % 3, num)

def solve_sudoku(arr):
    l = [0, 0]

    if (not find_empty_location(arr, l)):
        return True

    row = l[0]
    col = l[1]

    for num in range(1, 10):

        if (check_location_is_safe(arr, row, col, num)):

            arr[row][col] = num

            if (solve_sudoku(arr)):
                return True

            arr[row][col] = 0

    return False

if __name__ == "__main__":

    grid = [[0 for x in range(9)] for y in range(9)]

    grid = [[int(ele) for ele in input().split()] for i in range(9)]

    if (solve_sudoku(grid)):
        print("true")
    else:
        print("false")
