
with open('input.txt', 'r') as f:
    grid = []
    for l in f:
        line = list(l.strip())
        grid.append(line)

def isRoll(grid, row, column) -> bool:
    return grid[row][column] == "@"

def canRemove(total: int) -> bool:
    return total < 4 

def removeRolls(grid: list) -> int:
    rolls_to_remove = 0
    for row in grid:
        for column in row:
            if not isRoll(grid,row,column):
                continue
            else:
                ...


    return rolls_to_remove



