def adjList(n, m):
    adj_lst = {i: [] for i in range(0, n + 1)}

    for i in range(m):
        ui, vi, wi = map(int, inp.readline().strip().split())
        adj_lst[ui].append((vi, wi))

    return adj_lst

inp = open('Lab 4/Task 1/input1b.txt','r')
out = open('Lab 4/Task 1/output1b.txt','w')

n, m = map(int, inp.readline().strip().split())

adj_list = adjList(n, m)

for vrtx, nhbr in adj_list.items():
    print(f'{vrtx} : ', end='',file=out)
    for n, wght in nhbr:
        print(f' ({n},{wght})', end='',file=out)
    print(file=out)

