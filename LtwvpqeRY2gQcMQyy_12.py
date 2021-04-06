
def sig_figs(num):
    
    a,z=list(num), ["0","-","."]
    for i in a:
        if not i in z:
            if a[0]=="-": a=a[1:]
            if a[0]=="0":a=a[1:]
            if  "." in a:
                for i in a:
                    if i == ".": a.remove(i)
                b= int("".join(a))   
            elif not "." in a: b=int("".join(a[::-1]))
            return (len(list(str(b))))
    return 0

