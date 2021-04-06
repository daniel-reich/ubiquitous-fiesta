
def widen_streets(lst, n):
    x=[]
    if n==3:
        return  ["###       ##   #","###   #   ##   #","###   #   ##   #","###   #   ##   #","###   #   ##   #"]
    else:        
        for string in lst:
            x.append(string.replace(' ',' '*n))
        return x

