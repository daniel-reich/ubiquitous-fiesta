
def replace_next_largest(lst):
    a = sorted([(i[1], i[0]) for i in enumerate(lst)]) 
    a.append((-1, max(i[1] for i in a)+1))
    b = [(a[i+1][0], a[i][1]) for i in range(len(a)-1)] 
    c = sorted((i[1], i[0]) for i in b)
    return [i[1] for i in c]

