
def sort_by_letter(lst):
    l = []
    for i in lst:
        for j in i:
            if j.isalpha():
                l.append(j)
    l.sort()
    for i in range(len(lst)):
        for j in range(len(l)):
            if l[j] in lst[i]:
                l[j] = lst[i]
​
​
​
    return l

