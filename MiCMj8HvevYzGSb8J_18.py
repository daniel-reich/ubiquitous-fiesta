
def fibo_word(n):
    if n<2:return "invalid"
    l=["b","a"]
    for x in range(1,n-1):l.append(l[x]+l[x-1])
    return ", ".join(l)

