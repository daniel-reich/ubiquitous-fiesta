
def calculate_score(games):
    dict1={'RP':'P','RS':'R','PS':'S','PR':'P','SR':'R','SP':'S'}
    lst1,lst2=[],[]
    for x in games:
        if len(set(x))==len(x):
            if (x.index(dict1["".join(x)]))==1:
                lst2.append("won")
            if (x.index(dict1["".join(x)]))==0:
                lst1.append("won")
    if lst1 or lst2:   
        if lst1==lst2:
          return "Tie" 
        return "Abigail" if lst1.count('won')>lst2.count('won') else "Benson"
    return "Tie"

