lst = list(map(int, input().split()))

counter = []

for i in range(101):
    counter.append(0)

for i in range(len(lst)):
    counter[lst[i]] += 1

res = []

for i in range(len(counter)):
    if counter[i] > 0:
        for j in range(counter[i]):
            res.append(i)

for i in range(len(res)):
    print(res[i], end=" ")
