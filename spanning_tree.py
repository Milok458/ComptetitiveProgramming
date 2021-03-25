n = int(input())

coordinates = []

for i in range(n):
    curr = [int(item) for item in input().split()]
    coordinates.append(curr)

k = [28285] * n

p = [-1] * n

mst = [False] * n

k[0] = 0

q = []

for i in range(n):
    q.append(i)

while q:
    m = 28285

    sel = 0
    c = 0

    for v in q:
        if k[v] < m and not (mst[v]):
            m = k[v]
            sel = c
        c += 1

    u = q.pop(sel)
    mst[u] = True

    for j in range(n):
        if u != j and not (mst[j]):
            eu = ((((coordinates[u][0] - coordinates[j][0]) ** 2) + (
                    (coordinates[u][1] - coordinates[j][1]) ** 2)) ** 0.5)
            if eu < k[j]:
                k[j] = eu
                p[j] = u

tot = 0

for i in range(1, n):
    if p[i] != -1:
        tot += k[i]

print(tot)
