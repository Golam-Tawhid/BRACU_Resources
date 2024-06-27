def dfs(grid, visited, row, col):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '#' or visited[row][col]:
        return 0

    visited[row][col] = True
    diamonds = 0

    if grid[row][col] == 'D':
        diamonds = 1

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dr, dc in directions:
        diamonds += dfs(grid, visited, row + dr, col + dc)

    return diamonds


inp = open('Lab 4/Task 6/input6.txt','r')
out = open('Lab 4/Task 6/output6.txt','w')

r, h = map(int, inp.readline().strip().split())

grid = [inp.readline().strip() for i in range(r)]

visited = [[False for i in range(h)] for j in range(r)]

maxDimonds = 0
for row in range(r):
    for col in range(h):
        if grid[row][col] == 'D' and not visited[row][col]:
            maxDimonds = max(maxDimonds, dfs(grid, visited, row, col))
            
print(maxDimonds,file=out)