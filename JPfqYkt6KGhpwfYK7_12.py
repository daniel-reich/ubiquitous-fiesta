
def replace_the(st):
    st = st.split()
    lst = [i for i in range(len(st)) if st[i]=='the']
    for i in lst:
        if st[i+1][0] in 'aeiou':
            st[i]='an'
        else:
            st[i]='a'
    return ' '.join(st).strip()

