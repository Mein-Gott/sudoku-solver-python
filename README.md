# sudoku-solver-python
## Glossary
It's important to know a few terms before diving into the code:
- `cell` = the smallest square with the number
- `region` = a 3x3 sub-grid
- `given` = an initially defined number
- `group` = a row, a column or a region
- `candidate` = a possible value for a cell 
- `single` = the only candidate for a cell

[Wikipedia Sudoku Glossary](https://en.wikipedia.org/wiki/Glossary_of_Sudoku)  

My own meanings:  
- `final grid` = the grid is either complete or classified as impossible, further solving isn't relevant
