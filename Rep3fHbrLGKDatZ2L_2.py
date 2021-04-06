
def complete_pattern(s):
    for i in sorted(list(set(s))):
        sc=s
        if i!='_':
            sc=sc.replace('_',i)
            for j in range(1,len(sc)//2+1):
                x=sc[:j]
                r=len(sc)%len(x)
                if (len(sc)//len(x))*x+sc[len(sc)-r:]==sc:
                    return i

