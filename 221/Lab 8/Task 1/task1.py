import heapq

cost=0

def addedge(parent, u, v, w):
    global cost
    if fparent(parent, u) != fparent(parent, v):
        cost+=w
    parent[fparent(parent, v)] = parent[fparent(parent, u)]

def fparent(parent, u):
    if u == parent[u]:
        return u
    parent[u] = fparent(parent, parent[u])
    return parent[u]

inp = open('Lab 8/Task 1/input1.txt','r')
out = open('Lab 8/Task 1/output1.txt','w')

n, m = map(int, inp.readline().strip().split())
parent = [i for i in range(n+1)]
edge = []

for i in range(m):
    u,v, w= map(int, inp.readline().strip().split())
    heapq.heappush(edge, (w, u, v))
while edge:
    w,u,v = heapq.heappop(edge)
    addedge(parent, u, v, w)
print(cost, file=out)