
def anagram(name, words):
    count = 0
    st = ""
    st1 = ""
    for x in name:
        if x.isalpha():
            st = st+ x.lower()
    st = list(st)
    st.sort()
    st = "".join(st)
    for y in words:
        for a in y:
            st1 = st1 + a.lower()
    st1 = list(st1)
    st1.sort()
    st1 = "".join(st1)
    
    if st == st1:
        return True
    else:
        return False

