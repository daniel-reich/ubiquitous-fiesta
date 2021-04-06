
def max_possible( n1, n2):
    l1 = list(map(int, list(str(n1))))
    l2 = sorted(map(int, list(str(n2))), reverse=True)
    lo = []
    for index in range(0, len(l1)):
        if not l2:
            lo.append(l1[index])
            continue
        if l2[0] > l1[index]:
            lo.append(l2.pop(0))
        else:
            lo.append(l1[index])
    no = lo[0]
    for index in range(1, len(lo)):
        no = no*10 + lo[index]
    return no

