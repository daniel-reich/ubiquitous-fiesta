
def shadow_sentence(a, b):
    [a,b]=[a.split(' '),b.split(' ')]
    if len(a)!=len(b):return False
    return all([len(a[i])==len(b[i]) and len(set(a[i]).intersection(set(b[i])))==0 for i in range(len(a))] )

