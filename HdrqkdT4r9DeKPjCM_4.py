
def is_polygonal(n):
    if n == 1:
        return "0th of all"
    res = []
    for k in range(3,n):
        if -1/2 + (1/4 + (2*n-2)/k)**0.5 == int(-1/2 + (1/4 + (2*n-2)/k)**0.5):
            i = int(-1/2 + (1/4 + (2*n-2)/k)**0.5)
            print(i,k)
            if i%10 == 1 and i != 11:
              res.append("{}st {}-gonal number".format(i,k))
            elif i%10 == 2 and i != 12:
              res.append("{}nd {}-gonal number".format(i,k))
            elif i%10 == 3 and i != 13:
              res.append("{}rd {}-gonal number".format(i,k))
            else:
                res.append("{}th {}-gonal number".format(i,k))
    return False if res == [] else res
​
print(is_polygonal(4))

