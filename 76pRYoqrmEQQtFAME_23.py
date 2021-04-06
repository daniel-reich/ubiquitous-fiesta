
def is_astonishing(num):
    res, n = "", str(num)
    for i in range(1, len(n)):
        a,b = int(n[:i]), int(n[i:])
        (a,b), res = (sorted([a,b]), "BA") if a>b else ((a,b), "AB")
        if (b-a+1)*(a+b)/2 == num:
            return "{}-Astonishing".format(res)
    return False

