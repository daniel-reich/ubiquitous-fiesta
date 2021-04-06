
def alph_num(txt):
    lst=[]
    st=""
    for n in txt:
        lst.append(ord(n))
    for i in lst:
        st=st+" "+str(i-65)
        
    return st.strip()

