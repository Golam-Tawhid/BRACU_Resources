def adjMatrix(n, matrix):
    for i in range(0, n + 1):
        for j in range(0, n + 1):
            print(matrix[i][j], end=' ', file=out)
        print(file=out)

inp = open('Lab 4/Task 1/input1a.txt','r')
out = open('Lab 4/Task 1/output1a.txt','w')

n, m = map(int, inp.readline().strip().split())

matrix = [[0 for i in range(n + 1)] for j in range(n + 1)]

for i in range(m):
    ui, vi, wi = map(int, inp.readline().strip().split())
    matrix[ui][vi] = wi

adjMatrix(n, matrix)