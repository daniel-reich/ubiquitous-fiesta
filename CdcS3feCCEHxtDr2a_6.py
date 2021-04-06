
def clear_ordering(orders: list) -> bool:
    s1, s2 = set(), set()
    for i in orders:
        s1.add(i[0])
        s2.add(i[1])
    return len(s1) == len(s2) and len(s1.intersection(s2)) == len(s2) - 1

