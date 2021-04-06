
def josephus(people):
    lst = list(range(1, people + 1))
    count = 0
    while lst.count(0) != people - 1:
        for x in range(len(lst)):
            if lst[x] != 0:
                count += 1
                if count == 2:
                    lst[x] = 0
                    count = 0
    for x in lst:
        if x != 0:
            return x

