def dfs1(graph, vertex, stack, visited):
    visited[vertex] = True
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs1(graph, neighbor, stack, visited)
    stack.append(vertex)

def dfs2(graph, vertex, component, visited):
    visited[vertex] = True
    component.append(vertex)
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs2(graph, neighbor, component, visited)

def find_strongly_connected_components(N, edges):
    graph = {i: [] for i in range(1, N + 1)}
    reversed_graph = {i: [] for i in range(1, N + 1)}

    for u, v in edges:
        graph[u].append(v)
        reversed_graph[v].append(u)

    stack = []
    visited = [False] * (N + 1)

    # First DFS to find the finishing times
    for vertex in range(1, N + 1):
        if not visited[vertex]:
            dfs1(graph, vertex, stack, visited)

    # Reset visited for the second DFS
    visited = [False] * (N + 1)
    strongly_connected_components = []

    # Second DFS to find the strongly connected components
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            component = []
            dfs2(reversed_graph, vertex, component, visited)
            strongly_connected_components.append(component)

    return strongly_connected_components

# Sample Input 1
N1, M1 = 5, 5
edges1 = [(1, 2), (2, 3), (2, 4), (3, 1), (4, 5)]
print(*find_strongly_connected_components(N1, edges1))  # Output: [1, 2, 3], [4], [5]

# Sample Input 2
N2, M2 = 4, 3
edges2 = [(1, 2), (2, 3), (2, 4)]
print(*find_strongly_connected_components(N2, edges2))  # Output: [1], [2], [3], [4]
