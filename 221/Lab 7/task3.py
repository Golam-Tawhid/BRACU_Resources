def addedge(parent, size, u, v):
    if fparent(parent, u) != fparent(parent, v):
        size[fparent(parent, u)] += size[fparent(parent, v)]
    
    parent[fparent(parent, v)] = parent[fparent(parent, u)]

def fparent(parent, u):
    if u == parent[u]:
        return u
    parent[u] = fparent(parent, parent[u])
    return parent[u]


inp = open('Lab 7/Task 3/input3.txt','r')
out = open('Lab 7/Task 3/output3.txt','w')

n, k = map(int, inp.readline().strip().split())
parent = [i for i in range(n+1)]
size= [1]*(n+1)

for i in range(k):
    u,v= map(int, inp.readline().strip().split())
    addedge(parent, size, u, v)
    print(size[fparent(parent, u)],file=out)