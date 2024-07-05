def countWay(n):
    if n <= 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

inp = open('Lab 8/Task 2/input2.txt','r')
out = open('Lab 8/Task 2/output2.txt','w')

n = int(inp.readline())
print(countWay(n), file=out)