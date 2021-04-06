
def elasticize(st):
    if len(st)==1:
        return st
    if len(st)%2:
        splt = st.split(st[int(len(st)/2)])
        pivot_index = int(len(st)/2)
        left = ''.join([(i*a) for i,a in enumerate(splt[0],start=1)])
        pivot = st[pivot_index]
        pivot = pivot*(pivot_index+1)
        right = ''.join([(i*a) for i,a in enumerate(splt[1][::-1],start=1)])[::-1]
        return left + pivot + right
    elif len(st)%2==0:
        pivot1 = st[int(len(st)/2)]
        pivot2 = st[int(len(st)/2)-1]
        pivot = pivot2 + pivot1
        rep = st.index(st[int(len(st)/2)-1])+1
        main_pivot=''.join([a*rep for a in pivot])
        splt = st.split(pivot)
        left = ''.join([(i*a) for i,a in enumerate(splt[0],start=1)])
        right = ''.join([(i*a) for i,a in enumerate(splt[1][::-1],start=1)])[::-1]
        return left + main_pivot + right

