
def add_odd_to_n(n):
    total = 0
    lst = []
    for i in range(n + 1):
        if i % 2 != 0:
            lst.append(i)
            total =sum(lst)
    return total

