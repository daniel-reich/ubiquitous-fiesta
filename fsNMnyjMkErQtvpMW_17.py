
def holes(n):
    h=0
    for i in str(n):
        h+=1*(i in '4690')+2*(i=='8')
    return h
def holey_sort(lst):
    d=[(lst[i],holes(lst[i])) for i in range(len(lst))]
    d = sorted(d,key=lambda x: (x[1]))
    return [d[i][0] for i in range(len(d))]

