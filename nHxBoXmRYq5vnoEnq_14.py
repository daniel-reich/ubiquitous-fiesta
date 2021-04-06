
def vowels(string):
    a=["a","e","i","o","u"]
    b=[]
    for i in string:
        if i in a:
            b.append(i)
    return len(b)

