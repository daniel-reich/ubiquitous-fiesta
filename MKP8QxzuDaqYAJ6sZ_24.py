
def is_correct_aliases(names, aliases):
    if len(names) != len(aliases):
        return False
    for i in range(len(names)):
        name = names[i]
        alias = aliases[i].split()
        if len(alias) != 2:
            return False
        letter = name[0].upper()
        if (not 'A' <= alias[0][0] <= 'Z') or (not 'A' <= alias[1][0] <= 'Z') or \
           alias[0][0] != letter or alias[1][0] != letter:
            return False
    return True

