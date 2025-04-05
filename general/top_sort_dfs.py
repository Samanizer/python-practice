def top_sort_dfs(num_nodes, edges):
    graph = {n: [] for n in range(num_nodes)}
    for crs, dep in edges:
        graph[dep].append(crs)
    visited = {n: 0 for n in range(num_nodes)}
    stack = []

    def dfs(node):
        visited[node] = 1
        for neighbor in graph[node]:
            if visited[neighbor] == 1:
                return False
            if visited[neighbor] == 0:
                if not dfs(neighbor):
                    return False
        visited[node] = 2
        stack.append(node)
        return True
    
    for num in range(num_nodes):
        if visited[num] == 0:
            if not dfs(num):
                return []

    return stack[::-1]

prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
numCourses = 4

print(top_sort_dfs(numCourses, prerequisites))
