dims = [int(item) for item in input().split()]

n = dims[0]
k = dims[1]

ways = [1]

for i in range(1, k + 1):
    w = 0
    for j in reversed(range(i)):
        w += ways[j]
    ways.append(w)

for i in range(k + 1, n):
    new_way = 0
    for j in range(1, k + 1):
        new_way += ways[i - j]
    ways.append(new_way)

print(ways[n - 1])
