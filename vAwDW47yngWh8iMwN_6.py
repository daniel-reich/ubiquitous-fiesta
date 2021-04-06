
def cap_last(st):
    l2 = []
    for a in st.split():
        l1 = []
        for b in a:
            l1.append(b)
        l1[-1] = l1[-1].upper()
        l2.append(''.join(l1))
    return ' '.join(l2)

