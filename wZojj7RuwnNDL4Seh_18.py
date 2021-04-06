
def completely_filled(lst):
    brojac = 0
    for i in lst:
        for j in i:
            if(j == " "):
                brojac+=1
    res = False            
    if(brojac == 0):
        res=True
    else:
        res = False
    return res;

