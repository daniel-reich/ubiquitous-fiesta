
def find_a_seat(n, lst):
    m_cap = n // len(lst)
    res = [lst.index(x) for x in lst if (x <= m_cap * 0.5)]
    if res:
        return res[0]
    else:
        return -1

