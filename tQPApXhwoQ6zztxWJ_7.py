
def get_prices(lst):
    m=[]
    for j in lst:
        s=j.split(" ")
        p=s[-1]
        m.append(p[2:-1])
    return list(map(float,m))

