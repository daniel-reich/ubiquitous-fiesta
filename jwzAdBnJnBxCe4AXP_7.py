
def rearranged_difference(num):
    s = str(num)
    t = []
    for i in s:
        t.append(i)
    t.sort()
    s1 = "".join(t)
    t.sort(reverse=True)
    s2 = "".join(t)
    return int(s2)-int(s1)
​
print(rearranged_difference(123445))

