
def two_product(lst, n):
    from itertools import permutations as p
    for i in p(lst, 2):
        if i[0] * i[1] == n:
            i = list(i)
            if i[0] > i[1]:
                temp = i[1]
                i[1] = i[0]
                i[0] = temp
            return i

