
def make_change(r):
    dict = {}
    coins = [(25,'q'),(10,'d'),(5,'n'),(1,'p')]
    for c,n in coins:
        q,r = divmod(r,c)
        dict[n] = q
    return dict

