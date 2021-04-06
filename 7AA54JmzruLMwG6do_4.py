
def is_icecream_sandwich(txt):
    if not len(set(txt)) == 2:
        return False
    return txt.count(txt[0]) % 2 == 0

