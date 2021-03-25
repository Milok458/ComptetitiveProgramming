s = 0

dim = [int(item) for item in input().split()]

n = dim[0]
k = dim[1]

arr = [int(item) for item in input().split()]

arr = [1] + arr + [1]

negatives = []


def path_sum(start, finish):
    m = finish - start + 1

    p = []
    ways = [0] * m

    for j in range(k):
        ways[j] = arr[j + start]
        p.append([j + start])

    for j in range(k, m):
        sel = max(ways[j - k:j])
        ways[j] = sel + arr[j + start]
        p.append(p[ways.index(sel, j - k, j)] + [j + start])

    final = max(ways[m - k:m])

    return [final, p[ways.index(final, m - k, m)]]


for i in range(0, n):
    if arr[i] < 0:
        negatives.append(i)

path = []
c = 0

while c < n:
    if len(negatives) > 0 and c == negatives[0]:
        curr = negatives[0]
        counter = 1
        while counter < len(negatives) and negatives[counter] == curr + 1:
            curr = negatives[counter]
            counter += 1
        if counter >= k:
            res = path_sum(c, curr)

            s += res[0]

            path = path + res[1]

            c = curr + 1
            s += arr[c]
            path.append(c)
            c += 1
        else:
            c += counter
            s += arr[c]
            path.append(c)
            c += 1
        negatives = negatives[counter:]
    else:
        s += arr[c]
        path.append(c)
        c += 1

s += -2

jumps = len(path) - 1

print(s)
print(jumps)
for i in range(jumps + 1):
    print(path[i] + 1, end=" ")

