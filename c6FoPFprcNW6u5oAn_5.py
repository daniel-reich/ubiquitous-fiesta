
def farey(n):
    lst = ["0/1"]
    secondlst = [0]
    for i in range(1, n + 1):
        for o in range(1, i):
            if round(o / i, 10) in secondlst:
                continue
            else:
                lst.append(str(o) + "/" + str(i))
                secondlst.append(round(o / i, 10))
    sortedlst = [x for _, x in sorted(zip(secondlst, lst))]
    sortedlst.append("1/1")
    return sortedlst

