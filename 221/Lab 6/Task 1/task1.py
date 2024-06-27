import heapq

def shortestPath(n, edg, src):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in edg:
        graph[u].append((v, w))
    
    distance = {i: float('inf') for i in range(1, n + 1)}
    distance[src] = 0
    heap = [(0, src)]
    
    while heap:
        dist, node = heapq.heappop(heap)
        if dist > distance[node]:
            continue
        for nhbr, wght in graph[node]:
            new_dist = distance[node] + wght
            if new_dist < distance[nhbr]:
                distance[nhbr] = new_dist
                heapq.heappush(heap, (new_dist, nhbr))
    
    return [distance[i] if distance[i] != float('inf') else -1 for i in range(1, n + 1)]


inp = open('Lab 6/Task 1/input1.txt','r')
out = open('Lab 6/Task 1/output1.txt','w')

n, m = map(int, inp.readline().strip().split())
edg = []

for i in range(m):
    a= tuple(map(int, inp.readline().strip().split()))
    edg.append(a)

src = int(inp.readline())
shortpth = shortestPath(n, edg, src)
print(*shortpth, file=out)