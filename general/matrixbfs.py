from collections import deque

def shortestPath(grid, sr, sc, tr, tc):
    if grid[sr][sc] == 0 or grid[tr][tc] == 0:
        return -1
    if (sr, sc) == (tr, tc):
        return 0
    
    queue = deque([(sr,sc,0)])
    visited = set()
    visited.add((sr,sc))
    
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    while queue:
        row, col, steps = queue.popleft()
        if (row, col) == (tr, tc):
            return steps
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < len(grid) and
                0 <= new_col < len(grid[0]) and
                (new_row, new_col) not in visited and
                grid[new_row][new_col] == 1):
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, steps + 1))
    
    return -1

grid = [
    [1, 1, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 1, 1]
]

print(shortestPath(grid, 0, 0, 2, 3))  # Output: 5
print(shortestPath(grid, 0, 0, 1, 3))  # Output: -1 (Unreachable)
print(shortestPath(grid, 0, 0, 0, 0))
print(grid[-2][-2])
                    