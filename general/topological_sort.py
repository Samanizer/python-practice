from collections import deque

def topological_sort(num_nodes, edges):
    graph = {}
    in_degree = {}
    for num in range(num_nodes):
        graph[num] = []
        in_degree[num] = 0
    for crs, dep in edges:
        graph[dep].append(crs)
        in_degree[crs] += 1
    
    queue = deque([x for x in in_degree.keys() if in_degree[x] == 0])

    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result if len(result) == num_nodes else []
    

prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
numCourses = 4

print(topological_sort(numCourses, prerequisites))