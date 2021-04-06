
def is_correct_aliases(names, aliases):
    for value, name in enumerate(names):
        i = aliases[value]
        for a in i.split():
            if list(a)[0] != list(name)[0]:
                return(False)
    return(True)

