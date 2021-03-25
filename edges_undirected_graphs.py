n = int(input())

adj_mat = []

for i in range(n):
    adj_mat.append([int(item) for item in input().split()])

v = 0

for i in range(n):
    for j in range(i, n):
        if adj_mat[i][j] == 1:
            v += 1

print(v)
