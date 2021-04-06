
def last_ancestor(folders, X, Y):
​
    def up(x):
        for k, v in folders.items():
            if x in v: return k
        return x
​
    lx, ly = [X], [Y]
    for i in range(3):
        lx += up(lx[-1])
        ly += up(ly[-1])
​
    for i in lx:
        for j in ly:
            if i == j:
                return(i)
​
    #it's very inefficient but it works...

