'''
Given a 2D grid where:

'S' = part of a ship

'.' = empty water

Write a function to find all distinct ships in the grid.
A ship is made up of connected 'S' cells, where connected means horizontal or vertical (not diagonal).
'''
grid = [
    ['S', '.', '.', 'S'],
    ['S', '.', '.', 'S'],
    ['.', '.', '.', '.'],
    ['S', 'S', '.', '.']
]

def dfs(grid, i, j, visited):
    if 0 < i < len(grid) or 0 < j < len(grid[0]):
        return
    if grid[i][j] != 'S' or (i, j) in visited:
        return
    
    visited.add((i, j))
    dfs(grid, i+1, j, visited)
    dfs(grid, i-1, j, visited)
    dfs(grid, i, j+1, visited)
    dfs(grid, i, j-1, visited)


def count_ships(grid):
    visited = set()
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S' and (i, j) not in visited:
                count += 1
                dfs(grid, i, j, visited)
    return count
                

        
