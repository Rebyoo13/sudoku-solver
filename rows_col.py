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

def possible(x,y,n):
    for i in range(0,9): 
        if grid[i][x] == n: #verificam daca exista pe linie/orizontal
           return False

    for i in range(0,9):
        if grid[y][i] == n: #verificam pe coloane/verticala acum
            return False
        
    #cum ne uitam la fiecare numar de pe langa(dar sa fie in matricea de 3x3 ca poate sa fie si in colt)
    #cu indicii calculam indicii astfel incat sa caute mereu de la inceputul fiecarui patratel
    #rest rotunjit ori 3
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for X in range(x0, x0 + 3): #limite patrat vertical
        for Y in range(y0, y0 + 3): #limite patrat orizontal
            if grid[Y][X] == n:
                return False
    return True

def Print(matrix):
    for i in range(9):
        print(matrix[i]) 

def solve(): #functia de backtracking
    for y in range(9): 
        for x in range(9): 
            if grid[y][x] == 0: #nu poti sa ai 0, trebuie modificat
                for n in range(1,10):
                    if possible(x, y, n):
                        grid[y][x] = n #va incepe cu 1 daca e posibil
                        solve()
                        grid[y][x] = 0 #daca e 0, va incepe iarasi, o sa dea solve atata timp cat e n mai sus
                return 
    Print(grid)
    input("More?")

solve()
