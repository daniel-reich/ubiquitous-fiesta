
def shift_sentence(txt):
​
    l = txt.split()
    last =  l[-1][0] 
    n = []
    for i in range(1, len(l)):
        n.append(l[i - 1][0] + l[i][1:])
    n = [last + l[0][1:]] + n
    txt_2 = " ".join(n)
        
    return txt_2

