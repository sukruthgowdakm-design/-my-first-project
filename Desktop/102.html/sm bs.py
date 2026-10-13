from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {
    1: [2, 3],
    3: [1,5,6],
    2: [1,4],
    4: [2,7,8],
}

print("BFS Traversal:")
bfs(graph, 0)