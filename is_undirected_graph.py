n = int(input())

adj_mat = []

for i in range(n):
    adj_mat.append([int(item) for item in input().split()])

source = []
sink = []

for i in range(n):
    source.append(i)
    sink.append(i)

for i in range(n):
    for j in range(n):
        if adj_mat[i][j] == 1:
            for node in source:
                if node == j:
                    source.remove(node)
                    break
            for node in sink:
                if node == i:
                    sink.remove(node)
                    break

for node in source:
    print(node + 1, end=" ")

print("")

for node in sink:
    print(node + 1, end=" ")
