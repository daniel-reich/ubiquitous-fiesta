
def sorting(s):
        c,d,e,f,g,j=[],[],[],[],[],0
        for i in range(0,len(list(s))):
                try :int(list(s)[i])
                except ValueError:c.append(list(s)[i])
                else:d.append(list(s)[i])
        for i in range(0,len(c)):
                if ord(c[i])<97:e.append(c[i])
                else:f.append(c[i])
        f=sorted(f)
        e=sorted(e)
        while j <len(e):
                for i in range(0,len(f)):
                        if ord(e[j].lower())< ord(f[i]):
                                f.insert(i,e[j])
                                break
                j+=1
        if ord(e[-1].lower())>=ord(f[-1].lower()):f.append(e[-1])
        return "".join(f+sorted(d))

