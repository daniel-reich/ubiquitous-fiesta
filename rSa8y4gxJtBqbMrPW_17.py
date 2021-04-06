
def lcm(n1, n2):
    num = max([x for x in range(1, max(n1, n2) + 1) if n1 % x == 0 and n2 % x == 0])
    return int(num * n1/num * n2/num)

