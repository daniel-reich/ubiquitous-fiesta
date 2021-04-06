
def ascending(txt):
    l = len(txt)
    #make list of products:
    products = [i for i in range(2, l+1) if l % i == 0]
​
    #check if concursive and ascending when split up in x:
    def check(txt, x):
        ind = [i for i in range(0, l, l // x)]
        r = [int(txt[ind[i] : ind[i] + l // x]) for i in range(x)]
        return all(True if r[i] == r[i + 1] - 1 else False for i in range(x - 1))
​
    return any(check(txt, i) for i in products)

