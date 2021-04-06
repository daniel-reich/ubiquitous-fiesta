
def count_towers(towers):
    a=[]
    for i in towers:
        b=(" ".join(i))
        c=(b.split())
        a.append(len(c))
    return max(a)

