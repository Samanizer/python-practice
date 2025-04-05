from collections import deque

def grid_traverse(grid):
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    row = 0
    while row < len(grid):
        col = 0  # Reset col for each new row
        while col < len(grid[0]):
            print(f"Current: ({row},{col}) -> {grid[row][col]}")
            for r, c in directions:
                new_row = row + r
                new_col = col + c
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                    print(f"  Neighbor ({new_row},{new_col}): {grid[new_row][new_col]}")
            col += 1
        row += 1

def bfs(grid):
    directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    queue = deque([(0,0)])
    visited = set([(0,0)])
    result = []
    
    while queue:
        row, col = queue.popleft()
        result.append(grid[row][col])
        for r, c in directions:
            new_row = row + r
            new_col = col + c
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                if (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col))
    
    return result
    

# Test case
grid = [[1, 2, 3], [4, 5, 6]]
grid_traverse(grid)
print(bfs(grid))

grid = [[1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]]

print(bfs(grid))
