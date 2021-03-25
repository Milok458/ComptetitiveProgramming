dims = [int(item) for item in input().split()]

n = dims[0]
m = dims[1]

adj_mat = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    adj_mat.append(row)

for i in range(m):
    v = [int(item) for item in input().split()]
    adj_mat[v[0] - 1][v[1] - 1] = 1
    adj_mat[v[1] - 1][v[0] - 1] = 1

for i in range(n):
    for j in range(n):
        print(adj_mat[i][j], end=" ")
    print("")
