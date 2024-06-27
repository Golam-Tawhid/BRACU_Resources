import heapq

def dijkstra(graph, st, dest):
    distance = [float('inf')] * (len(graph) + 1)
    distance[st] = 0
    pq = [(0, st)]

    while pq:
        dist, node = heapq.heappop(pq)
        if node == dest:
            return dist

        for nhbr, wght in graph[node]:
            new_dist = max(dist, wght)
            if new_dist < distance[nhbr]:
                distance[nhbr] = new_dist
                heapq.heappush(pq, (new_dist, nhbr))

    return -1

inp = open('Lab 6/Task 3/input3.txt','r')
out = open('Lab 6/Task 3/output3.txt','w')

n, m = map(int, inp.readline().strip().split())
graph = [[] for i in range(n + 1)]

for i in range(m):
    u, v, w = map(int, inp.readline().strip().split())
    graph[u].append((v, w))

min_danger = dijkstra(graph, 1, n)

# Output the result
if min_danger == -1:
    print("Impossible", file=out)
else:
    print(min_danger, file=out)
