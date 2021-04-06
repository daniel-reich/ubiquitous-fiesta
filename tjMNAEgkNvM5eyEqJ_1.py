
def unique_abbrev(abbs, words):
    for a in abbs:
        if sum(w.startswith(a) for w in words) != 1:
            return False
    return True

