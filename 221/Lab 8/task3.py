def minCoins(coins, x):
    dp = [float('inf')] * (x + 1)
    dp[0] = 0

    for i in range(1, x + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[x] if dp[x] != float('inf') else -1

inp = open('Lab 8/Task 3/input3.txt','r')
out = open('Lab 8/Task 3/output3.txt','w')

n, x = map(int, inp.readline().strip().split())

mCoin = list(map(int, inp.readline().strip().split()))

print(minCoins(mCoin, x), file=out)