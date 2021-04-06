
def calculate_score(lofs):
    a=0
    b=0
    for c in lofs:
        if c[0]!=c[1]:
            if c in [["R", "S"],["P", "R"],["S","P"]]:
                a+=1
            else:
                b+=1
    if a>b:
        return "Abigail"
    elif b>a:
        return "Benson"
    else:
        return 'Tie'

