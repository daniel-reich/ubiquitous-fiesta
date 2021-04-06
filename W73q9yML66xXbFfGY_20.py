
def coloured_triangle(row):
    r=row
    while len(r)>1:
        l=""
        for i in range(len(r)-1):
            s={"R","G","B"}
            if r[i]==r[i+1]:
                l+=r[i]
            else:
                s.remove(r[i])
                s.remove(r[i+1])
                l+=s.pop()
        r=l
    return r

