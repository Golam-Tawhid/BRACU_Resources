def cyclefind(grph, strt, visited, stack):
    visited[strt] = True
    stack[strt] = True

    for nhbr in grph[strt]:
        if not visited[nhbr]:
            if cyclefind(grph, nhbr, visited, stack):
                return True
        elif stack[nhbr]:
            return True

    stack[strt] = False
    return False


def cycle(grph, n):
    visited = [False] * (n + 1)
    stack = [False] * (n + 1)

    for vrtx in range(1, n + 1):
        if not visited[vrtx]:
            if cyclefind(grph, vrtx, visited, stack):
                return True

    return False


inp = open('Lab 4/Task 4/input4.txt','r')
out = open('Lab 4/Task 4/output4.txt','w')

n, m = map(int, inp.readline().strip().split())

grph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    u, v = map(int, inp.readline().strip().split())
    grph[u].append(v)

if cycle(grph, n):
    print("YES",file=out)
else:
    print("NO",file=out)
