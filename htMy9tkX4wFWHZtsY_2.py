
def palindrome_time(lst):
    h1, m1, s1 = lst[0:3]
    h2, m2, s2 = lst[3:]
    np = 0
    if m1 > 55:
        h1 += 1
        m1 = 0
    h1p = int(str(100 + h1)[-2::-1])
    for h in range(h1, h2 + 1):
        if 6 <= h % 10 <= 9:
            continue
        # only 00, 11, 22, 33, 44, 55 minutes can by palindromic
        mf = 0 if h != h1 else 11 * (m1 // 11) + (11 if m1 % 11 else 0)
        for m in range(mf, 60, 11):
            if h == h2 and (m > m2 or (h1 == h1 and m == m1 and not (s1 <= h1p <= s2))):
                break
            np += 1
    return np

