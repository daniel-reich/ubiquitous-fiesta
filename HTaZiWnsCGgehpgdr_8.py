
def license_plate(s, n):
    s_upper = "".join(c.upper() for c in s if c != "-")
    len_s = len(s_upper)
    lst_parts = [s_upper[max(-i * n + len_s, 0): (1 - i) * n + len_s]
                 for i in range(1, len_s // n + 1 + bool(len_s % n))]
    return "-".join(lst_parts[::-1])

