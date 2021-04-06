
def is_isomorphic(s, t):
    def r(s):
        x = sorted(list(set(list(s))),key=lambda x:s.index(x))
        obj = {}
        for char,i in enumerate(x):
            obj[i]=char
        return  obj
    s1 = r(s)
    t1 = r(t)
    return ''.join(list(map(lambda x:str(s1[x]),list(s)))) ==(''.join(list(map(lambda x:str(t1[x]),list(t)))))

