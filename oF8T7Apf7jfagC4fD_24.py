
def antipodes_average(lst):
    a = lst[0:int(len(lst)/2)]
    b = lst[int(len(lst)/2):][::-1]
    c = []
    for i in range(0,len(a)):
      c.append((a[i]+b[i])/2)
    return c

