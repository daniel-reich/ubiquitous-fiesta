
b=[]
def check_pattern(lst, pattern):
    import string as st
    global b 
    st=iter(st.ascii_uppercase)
    a={}
    ls=''
    for i in lst :
        if  str(i) not  in a  :
            a[str(i)]=next(st)
            ls=ls+a[str(i)]
        else  :
            ls=ls+a[str(i)]
    if a in b  :
      return ls[::-1]==pattern
    else : 
      b.append(a)
      return  ls==pattern

