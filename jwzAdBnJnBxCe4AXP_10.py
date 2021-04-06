
def rearranged_difference(num):
    a = []
    for ele in str(num):
        a.append(ele)
        l= "".join(sorted(a))
        j= "".join(sorted(a)[::-1])
    return int(j)-int(l)

