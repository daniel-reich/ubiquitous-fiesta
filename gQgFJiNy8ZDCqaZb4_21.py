
def overlap(s1, s2):
    for i in range(len(s1)):                  
        if s1[i:] == s2[:len(s1[i:])]:
            return s1[:i] + s2
    return s1 + s2

