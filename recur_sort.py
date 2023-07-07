def split_lst(lst):
    if len(lst) == 1:
        return lst
    n = len(lst) // 2
    lst = [split_lst(lst[:n]), split_lst(lst[n:])]
    return lst


def join_sort(lst):
    if len(lst) < 2:
        return lst
    f = []
    l1 = join_sort(lst[0])
    l2 = join_sort(lst[1])
    i1 = i2 = 0
    while True:
        if l1[i1] < l2[i2]:
            f.append(l1[i1])
            i1 += 1
            if i1 == len(l1):
                f.extend(l2[i2:])
                break
        else:
            f.append(l2[i2])
            i2 += 1
            if i2 == len(l2):
                f.extend(l1[i1:])
                break
    return f


num = list(map(int, input().split()))
num_sorted = join_sort(split_lst(num))
print(*num_sorted)

