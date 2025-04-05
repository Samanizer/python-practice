def numIslands(grid):
    if not grid:
        return 0
    
    def dfs(r, c):
        
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
            return
        
        grid[r][c] = 0
        
        directions = [(-1,0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            dfs(r + dr, c + dc)
    
    island_count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                island_count += 1
                dfs(row, col)
                
    return island_count

grid1 = [
    [1, 1, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [0, 1, 0, 0, 1]
]

grid2 = [
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1]
]

print(numIslands(grid1))  # Output: 5
print(numIslands(grid2))  # Output: 6
