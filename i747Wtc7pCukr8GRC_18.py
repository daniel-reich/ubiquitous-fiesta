
def max_product(lst):
    max_num = lst[0] * lst[1] * lst[2]
    for i in range(len(lst)):
        for x in range(len(lst)):
            for z in range(len(lst)):
                if max_num < lst[i] * lst[x] * lst[z] and not i == x and not i == z and not x == z:
                    max_num = lst[i] * lst[x] * lst[z]
    return max_num
​
​
​
​
def min_product(lst):
    max_num = lst[0] * lst[1] * lst[2]
    for i in range(len(lst)):
        for x in range(len(lst)):
            for z in range(len(lst)):
                if max_num > lst[i] * lst[x] * lst[z] and not i == x and not i == z and not x == z:
                    max_num = lst[i] * lst[x] * lst[z]
    return max_num

