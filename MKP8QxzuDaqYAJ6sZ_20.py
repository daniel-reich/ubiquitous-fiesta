
def is_correct_aliases(names, aliases):
    for name, alias in zip(names, aliases):
        i_name, i_surname = next(zip(*alias.split()))
        if not name[0] == i_name == i_surname: return False
    return True

