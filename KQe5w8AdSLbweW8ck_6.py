
def char_at_pos(r, s):
    k= [r[i] for i in range(0,len(r),2)] if s=="odd" else [r[j] for j in range(1,len(r),2)]
    if type(r)==str: k="".join(k)
    return k

