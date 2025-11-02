# Sudoku Solver 

A Python project that automatically solves Sudoku puzzles using the backtracking algorithm.  
The project includes two modes: `rows_col.py` (console-based solver) and `autogui.py` (automatically writes the solution into an external application).  

Demo:  
![Sudoku Screenshot](ss3.png)  

Link to project: [https://github.com/Rebyoo13/sudoku-solver](https://github.com/Rebyoo13/sudoku-solver)

---

## How It's Made
- Backtracking algorithm for solving Sudoku puzzles.  
- The `possible(x, y, n)` function checks Sudoku rules (row, column, 3x3 square).  
- `rows_col.py` displays the solution in the console.  
- `autogui.py` automatically inputs the solution using **PyAutoGUI**.
---

## Usage

### 1. Console Mode
```bash
python rows_col.py
````

* Define your Sudoku puzzle as a 9x9 matrix called 'grid'.
* Use 0 for empty cells that need to be filled.
* Example of grid format

```
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
```

* Run the script: it will solve the Sudoku and output the solution.

### 2. Automatic Input Mode

```bash
python autogui.py
```

1. Open Sudoku.com or any other Sudoku application where you want to input the solution.
2. Enter all 9 rows of the puzzle manually (use 0 for empty cells, for example: 040000000).
3. Make sure the top-left cell of the Sudoku grid is selected (cursor active) in the application.
4. Run this script. It will solve the puzzle and automatically input the solution into the application
   by simulating key presses and navigating between cells.
> Warning: Do not use the mouse or keyboard while `autogui.py` is running, or the automation may fail.
---

## Lessons Learned

* Understanding and implementing the backtracking algorithm.
* Automating keyboard and mouse actions using PyAutoGUI.
* Structuring a Python project and creating a clear, professional README.

````
