
def random(lst):
    A = []
    x0, x1 = lst
    a = 0
    while len(A) < 2 and a < 65535:
        if x1 == (a * x0 + 1) % 65535:
            A.append(a)
        a += 1
    return None if len(A) != 1 else (A[0] * lst[1] + 1) % 65535

