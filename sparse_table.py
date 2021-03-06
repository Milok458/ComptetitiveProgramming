def get_min(left, right):
    k = mp[right - left]
    return min(sparse[left][k], sparse[right - (1 << k)][k])


dims = [int(item) for item in input().split()]

n = dims[0]
m = dims[1]
a1 = dims[2]

bp = 1

while 1 << bp <= n:
    bp += 1

mp = [0] * (n + 1)

sparse = []

for i in range(n):
    row = []
    for j in range(bp):
        row.append(0)
    sparse.append(row)

ai = [0] * n

ai[0] = a1

for i in range(1, n):
    ai[i] = (23 * ai[i - 1] + 21563) % 16714589

for i in range(n):
    sparse[i][0] = ai[i]

for i in range(1, bp):
    for j in range(0, (n - (1 << i)) + 1):
        sparse[j][i] = min(sparse[j][i - 1], sparse[j + (1 << (i - 1))][i - 1])

for i in range(2, n + 1):
    mp[i] = mp[i // 2] + 1

vu = [int(item) for item in input().split()]

u = vu[0]
v = vu[1]

cr = max(v, u) - 1
cl = min(v, u) - 1

r = get_min(cl, cr + 1)

for i in range(1, m):
    u = ((17 * u + 751 + r + (2 * i)) % n) + 1
    v = ((13 * v + 593 + r + (5 * i)) % n) + 1

    cr = max(v, u) - 1
    cl = min(v, u) - 1

    r = get_min(cl, cr + 1)

print(u)
print(v)
print(r)
