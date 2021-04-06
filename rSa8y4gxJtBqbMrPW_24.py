
def lcm(n1, n2):
    if (n2%n1)==0:
        return n2
    else:
        c=[]
        a=[n1*i for i in range(n2+1)]
        b=[n2*j for j in range(n1+1)]
        for i in range(1,len(a)):
            for j in range(1,len(b)):
                if a[i]==b[j]:
                    c.append(a[i])
                    break
        return c[0]

