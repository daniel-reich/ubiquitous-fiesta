
def is_smooth(sentence):
    s = sentence.casefold().split()
    b = False
    for L in range(1, len(s)):
        if(s[L-1][-1] == s[L][0]):
            b = True
        else:
            b = False
            break
    return b

