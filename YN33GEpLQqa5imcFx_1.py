
def pascals_triangle(n):
    a=1
    s=[1]
    for i in range(1,n+1):
        a=a*(n+1-i)//i
        s.append(a)
    return " ".join([str(e) for e in s])

