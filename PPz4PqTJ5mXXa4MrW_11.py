
def ulam(n):
    lst = [1, 2]
    num = 3
    while len(lst) < n:
        count = 0
        for i in lst:
            if 2 * i > num and num - i in lst:
                count += 1
            if count > 1:
                break
        if count == 1:
            lst.append(num)
        num += 1
    return lst[-1]

