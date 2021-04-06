
def is_magic(s):
    n = len(s)
    if n == 0:
        return True
    n_max = n * n
    s_row = set()
    for row in s:
        if max(row) <= n_max and min(row) >= 1:
            s_row.add(sum(row))
        else:
            return False
    if len(s_row) != 1:
        return False
    m_num = s_row.pop()
    for col in zip(*s):
        if max(col) > n_max or min(col) < 1 or sum(col) != m_num:
            return False
    s1 = s2 = 0
    for i in range(n):
        s1 += s[i][i]
        s2 += s[i][n - 1 - i]
    return s1 == m_num and s2 == m_num

