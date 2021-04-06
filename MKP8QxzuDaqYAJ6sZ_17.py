
def is_correct_aliases(names, aliases):
    x=0
    c=1
    for a in names:
        if a[0]==aliases[x][0] and a[0]==aliases[x][aliases[x].find(' ')+1]:
            c=1
        else:
            c=0
            break
        x = x + 1
    if c==0:
        return False
    else:
        return True

