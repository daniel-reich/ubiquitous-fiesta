
def count_same_ends(st):
    import string
    pn = string.punctuation
    lst = []
    for a in st.split():
        s = ''
        for b in a:
            if not b in pn:
                s+=b.lower()
        lst.append(s)
    return sum((1 for a in lst if not len(a)==1 and a[0]==a[-1]))

