
def uncensor(txt, vowels):
    lst = []
    uncensored = ""
    for i in txt:
        lst.append(i)
    for i in vowels:
        for y in range(len(lst)):
            if lst[y] == "*":
                lst[y] = i
                break
    for i in lst:
        uncensored += i
    return uncensored

