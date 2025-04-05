"""
BFS 
Iterative

bfs
    if root is none             # special case
    return
    que, visited, results
    add to que
    if que is not empty
        process node (add to result)
        add its neighbors to que
    return result

"""
from collections import deque

def bfs_tree(root):
    
    if not root:
        return []
    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

def bfs_graph(graph, start):
    if start not in graph:
        return []

    queue = deque([start])
    visited = set([start])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return result

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(bfs_graph(graph, 'A'))

def shortest_path_bfs(graph, start, end):
    """
    Find the shortest path from `start` to `end` in an unweighted graph using BFS.
    Return the path as a list of nodes.

    start at start
    check if its same as end
    explore all neighbors - add them to a que to process
    check if end is there? - track the path
    keep exploring each neighbor's neighbors

    graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
    }

    """
    if start not in graph or end not in graph:
        return []
    queue = deque([start])
    result = []
    path_map = {start: None}

    while queue:
        node = queue.popleft()
        if node == end:
            break
        else:
            for neighbor in graph[node]:
                if neighbor not in path_map:
                    queue.append(neighbor)
                    path_map[neighbor] = node
    
    node = end

    while node is not None:
        result.append(node)
        node = path_map.get(node, None)
    
    result.reverse()
    return result

print(shortest_path_bfs(graph, 'A', 'F'))



