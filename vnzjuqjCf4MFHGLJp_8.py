
def shift_letters(txt, n):
    lst = [len(word) for word in txt.split()]
    st = txt.replace(" ", "")
    for x in range(n):
        st = st[-1] + st[:-1]
    s = 0
    for x in lst:
        st = st[:x + s] + " " + st[x + s:]
        s += x + 1
    return st.strip(" ")

