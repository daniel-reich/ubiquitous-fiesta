
def sum_digits(a, b):
    out = []
    for i in range(a,b + 1):
        i = str(i)
        for x in i:
            out.append(int(x))
    return sum(out)

