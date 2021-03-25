dim = list(map(int, input().split()))
n = dim[0]
m = dim[1]

table = []

for i in range(n):
    table.append([int(item) for item in input().split()])

dp = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(0)
    dp.append(row)

min_dmg = 0

for i in reversed(range(n)):
    for j in reversed(range(m)):
        if i == n - 1 and j == m - 1:
            min_dmg = 0
        else:
            if i == n - 1:
                min_dmg = dp[i][j + 1]
            else:
                if j == m - 1:
                    min_dmg = dp[i + 1][j]
                else:
                    min_dmg = min(dp[i + 1][j], dp[i][j + 1])

        dp[i][j] = min_dmg + table[i][j]

print(dp[0][0])
