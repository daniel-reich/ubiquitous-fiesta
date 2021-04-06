
def swap_cards(n1, n2):
    s1, s2 = str(n1), str(n2)
    lst1, lst2 = [int(s1[0]), int(s1[1])], [int(s2[0]), int(s2[1])]
    if lst1[0] == lst1[1]:
        lst1[0], lst2[0] = lst2[0], lst1[0]
    else:
        min1, idx1 = (lst1[0], 0) if lst1[0] < lst1[1] else (lst1[1], 1)
        lst1[idx1], lst2[0] = lst2[0], min1
    return 10 * lst1[0] + lst1[1] > 10 * lst2[0] + lst2[1]

