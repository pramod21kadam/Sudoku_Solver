from numpy import matrix
import re
#######################################################################################
grid = [
     [3,0,6,5,0,8,4,0,0],
     [5,2,0,0,0,0,0,0,0],
     [0,8,7,0,0,0,0,3,1],
     [0,0,3,0,1,0,0,8,0],
     [9,0,0,8,6,3,0,0,5],
     [0,5,0,0,9,0,6,0,0],
     [1,3,0,0,0,0,2,5,0],
     [0,0,0,0,0,0,0,7,4],
     [0,0,5,2,0,6,3,0,0]
 ]
solutions= list()
# Function to check input is correct at given position or not
def checkGrid( y , x , num):
    global grid
    #check X and Y direction
    for i in range(0,9):
        if grid[y][i] == num:
            return False
        if grid[i][x] == num:
            return False 

    x0 = (x//3)*3
    y0 = (y//3)*3

    #check square    
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j]== num:
                return False
    return True
# backTracking using recursion
def solve():
        for i in range(0,9):
            for j in range(0,9):
                if grid[i][j] == 0:
                    for k in range(1, 10):
                        if checkGrid(i,j,k):
                            grid[i][j] = k
                            solve()
                            grid[i][j] = 0
                    return
        solutions.append(matrix(grid))


solve()

file = open("Sudoku Solutions.txt",'w')
char = [ "[" , "]" , "," ]
l2 = []
for i in (solutions):
        file.write(str((i)))
file.close()
