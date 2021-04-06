
def remove_letters(st,c):
    for a in c:
        if a in st:
            st.pop(st.index(a))
    return st

