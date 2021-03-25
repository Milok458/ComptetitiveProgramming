def merge(lst_a, lst_b):
    res_lst = []

    while lst_a and lst_b:
        if lst_a[0] < lst_b[0]:
            res_lst.append(lst_a.pop(0))
        else:
            res_lst.append(lst_b.pop(0))

    while lst_a:
        res_lst.append(lst_a.pop(0))

    while lst_b:
        res_lst.append(lst_b.pop(0))

    return res_lst


def merge_sort(lst):
    if len(lst) == 1:
        return lst
    else:
        h = len(lst) // 2
        a = merge_sort(lst[:h])
        b = merge_sort(lst[h:])

        return merge(a, b)


n = int(input())
res = list(map(int, input().split()))

res = merge_sort(res)

for i in range(n):
    print(res[i], end=" ")
