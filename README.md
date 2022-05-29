# sudoku-solver-python
  
A python program able solve standard (9x9) sudoku puzzles.

## Installation
Clone the repo to your computer.

## Usage
1. Open the `play_with_it.py` file
2. Type your sudoku into the `starting_grid`
    - Each sublist represents a row
    - Zeros represent empty cells
3. Then just run the `play_with_it.py` file. The final grid is printed after a while.

## Glossary
Here are the key sudoku terms used in the code:
- `cell` = the smallest square with the number
- `region` = a 3x3 sub-grid
- `clue` = an initially defined number
- `group` = a row, a column or a region
- `candidate` = a possible value for a cell 
- `single` = the only candidate for a cell

[Wikipedia Sudoku Glossary](https://en.wikipedia.org/wiki/Glossary_of_Sudoku)  

My own meanings:  
- `final grid` = the grid is either complete or classified as impossible, further solving isn't possible
- `groupset` = all the groups of a given group type, for example all rows or all regions
- `illegal` = doesn't comply with the rules of sudoku 
