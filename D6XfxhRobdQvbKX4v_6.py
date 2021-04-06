
def first_before_second(st,w1,w2):
    s1 = []
    s2 = []
    for i in range(len(st)):
        if st[i]==w1:
            s1.append(i)
        elif st[i]==w2:
            s2.append(i)
    for a in s1:
        if a > s2[0]:
            return False
    return True

