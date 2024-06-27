def dfs(graph, vrtx, visited, stack):
    visited[vrtx] = True

    for nhbr in graph[vrtx]:
        if not visited[nhbr]:
            dfs(graph, nhbr, visited, stack)

    stack.append(vrtx)


def transpose(graph):
    transposed = {vrtx: [] for vrtx in graph}
    for vrtx in graph:
        for nhbr in graph[vrtx]:
            transposed[nhbr].append(vrtx)

    return transposed


def dfs_scc(graph, vrtx, visited, scc):
    visited[vrtx] = True
    scc.append(vrtx)

    for nhbr in graph[vrtx]:
        if not visited[nhbr]:
            dfs_scc(graph, nhbr, visited, scc)


def strongly_connected(num, edges):
    graph = {vrtx: [] for vrtx in range(1, num + 1)}
    for u, v in edges:
        graph[u].append(v)

    visited = [False] * (num + 1)
    stack = []

    for vrtx in range(1, num + 1):
        if not visited[vrtx]:
            dfs(graph, vrtx, visited, stack)

    transposed_graph = transpose(graph)
    visited = [False] * (num + 1)
    result = []

    while stack:
        vrtx = stack.pop()
        if not visited[vrtx]:
            scc = []
            dfs_scc(transposed_graph, vrtx, visited, scc)
            result.append(scc)

    return result

def print_result(components):
    for component in components:
        print(*component, file=out)

inp = open('Lab 5/Task 3/input3.txt','r')
out = open('Lab 5/Task 3/output3.txt','w')

n, m = map(int, inp.readline().strip().split())

edg = []

for i in range(m):
    a= tuple(map(int, inp.readline().strip().split()))
    edg.append(a)

result = strongly_connected(n, edg)
print_result(result)