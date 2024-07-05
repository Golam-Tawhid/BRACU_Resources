import heapq

def dijkstra(graph, st):
    distance = [float('inf')] * (len(graph) + 1)
    distance[st] = 0
    pq = [(0, st)]

    while pq:
        dist, i = heapq.heappop(pq)
        if dist > distance[i]:
            continue

        for nhbr, wght in graph[i]:
            new_dist = dist + wght
            if new_dist < distance[nhbr]:
                distance[nhbr] = new_dist
                heapq.heappush(pq, (new_dist, nhbr))

    return distance

def meet_point(graph, s, t):
    alice_dists = dijkstra(graph, s)
    bob_dists = dijkstra(graph, t)

    min_time = float('inf')
    meet_node = -1

    for i in range(1, len(graph)):
        if alice_dists[i] < float('inf') and bob_dists[i] < float('inf'):
            if alice_dists[i] >= bob_dists[i] and alice_dists[i]<min_time:
                min_time= alice_dists[i]
                meet_node = i
            elif alice_dists[i] <= bob_dists[i] and bob_dists[i]<min_time:
                min_time= bob_dists[i]
                meet_node = i
    return min_time, meet_node

inp = open('Lab 6/Task 2/input2.txt','r')
out = open('Lab 6/Task 2/output2.txt','w')

n, m = map(int, inp.readline().strip().split())
graph = [[] for i in range(n + 1)]

for i in range(m):
    u, v, w = map(int, inp.readline().strip().split())
    graph[u].append((v, w))
s, t = map(int, inp.readline().strip().split())

time, i = meet_point(graph, s, t)
if i == -1:
    print("Impossible", file=out)
else:
    print("Time", time, file=out)
    print("Node", i, file=out)