
def josephus(people):
    lst = [x for x in range(1, people + 1)]
    while len(lst) > 1:
        lst = lst[2:] + [lst[0]]
    return lst.pop()

