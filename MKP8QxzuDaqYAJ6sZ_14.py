
def is_correct_aliases(names, aliases):
    for i in range(len(names)):
        fl=names[i][0]
        if (aliases[i].split()[0][0]==fl.upper()) & (aliases[i].split()[1][0]==fl.upper()):
            continue
        else:
            return False
    return True

