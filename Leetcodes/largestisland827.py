
def largest_island(grid):
    max_size = 0
    
    visited = set()
    curr_island = 2
    size_map = {}
    
    def dfs(i, j):
        
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
            return 0
        
        if grid[i][j] != 1 or (i, j) in visited:
            return 0
        
        visited.add((i,j))
        grid[i][j] = curr_island
        size = 1
        
        dirs = [(0,-1), (0,1), (-1,0), (1,0)]
        for dr, dc in dirs:
            size += dfs(i + dr, j + dc )
        
        return size
    
    # first pass, label islands and fill size map
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in visited and grid[i][j] == 1:
                size_map[curr_island] = dfs(i, j)
                curr_island += 1

    max_size = max(size_map.values(), default=0)
    
    # try flipping zeroes and see
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            dirs = [(0,-1), (0,1), (-1,0), (1,0)]
            if grid[i][j] == 0:
                islands_found = set()
                for dr, dc in dirs:
                    ni, nj = i+dr, j+dc
                    
                    if grid[ni][nj] in size_map:
                        islands_found.add(grid[ni][nj])
                total_size = 0
                for island in islands_found:
                    total_size += size_map[island]
                max_size = max(max_size, total_size)

    return max_size