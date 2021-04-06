
def is_correct_aliases(names, aliases):
    names_l= [i[0] for i in names]
    for i in range(len(aliases)):
        aliases[i]=aliases[i].split(' ')
    aliases_l=[''.join(j[0] for j in i) for i in aliases]
    for i in range(len(names_l)):
        if set(names_l[i])!=set(aliases_l[i]): return False
    return True

