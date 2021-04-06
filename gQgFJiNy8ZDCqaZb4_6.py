
def overlap(s1, s2):
    z = ''
    for i in s1:
        if s1[s1.index(i):len(s1)] in s2:
            break
        elif s1[len(s1)-1] in s2[-1]:
            return s1+s2
        else: z+= s1[s1.index(i)]
    return z+s2

