grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def possible(x, y, n): #Python convetion is x = row, y = column
    for i in range(9):
        if grid[y][i] == n:
            return False
    for i in range(9):
        if grid[i][x] == n:
            return False
    x0 = (x //3 )* 3
    y0 = (y //3) * 3
    for i in range(x0, x0+3):
        for j in range(y0, y0+3):
            if grid[j][i] == n:
                return False
    return True #If n is not the the row/column/3x3 matrix, 0 becomes n

def print_function(matrix):
    for i in range(9):
        print(matrix[i])
        
def solution():
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(x,y,n): #Column, row, possible number
                        grid[y][x] = n
                        solution() #Recursion call, this is where the solution goes back to square 1(first element of matrix)
                        '''If there isn't any viable solution(on the last recursive call), the
                        called position or element is set to 0'''
                        grid[y][x] = 0
                return #We backtrack and we try the next number
    print_function(grid)
    
solution()