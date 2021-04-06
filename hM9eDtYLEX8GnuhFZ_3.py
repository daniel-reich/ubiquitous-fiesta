
def random(lst):
    x1, x2, r, k, n, t = lst[0], lst[1], [], 65535, 0, 0; a = (x2-1)/x1
    while a < k:
        if not a%1: r.append(a); t += 1
        if t > 1: break
        n += 1; a = (n*k + x2 - 1)/x1
    return None if t != 1 else int((r[0]*x2+1)%k)

