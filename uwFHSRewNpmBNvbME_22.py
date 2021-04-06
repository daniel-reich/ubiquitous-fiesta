
def same_vowel_group(w):
    vowels={"a","e","i","o","u"}
    l=[]
    s=set(w[0])
    k=s&vowels
    for i in range(0,len(w)):
        if k==set(w[i])&vowels:
            l.append(w[i])
    return l

