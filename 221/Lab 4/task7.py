def bfs(graph, start):
    queue = []
    visited = [False] * (len(graph) + 1)
    dstnce = [0] * (len(graph) + 1)

    queue.append(start)
    visited[start] = True

    while queue:
        current = queue.pop(0)

        for nhbr in graph[current]:
            if not visited[nhbr]:
                queue.append(nhbr)
                visited[nhbr] = True
                dstnce[nhbr] = dstnce[current] + 1

    return dstnce

inp = open('Lab 4/Task 7/input7.txt','r')
out = open('Lab 4/Task 7/output7.txt','w')
n = int(inp.readline())

graph = {i: [] for i in range(1, n + 1)}
for i in range(n - 1):
    u, v = map(int, inp.readline().strip().split())
    graph[u].append(v)
    graph[v].append(u)

leaf_nodes = [node for node in graph if len(graph[node]) == 1]
cityA = leaf_nodes[0]
distances = bfs(graph, cityA)
cityB = max(range(1, n + 1), key=lambda node: distances[node])

print(cityA, cityB, file=out)
