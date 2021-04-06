
def grant_the_hint(txt):
    lst = txt.split()
    longest = len(max(lst, key=len))
    ret = []
    for c in range(longest+1):
        ret.append(' '.join([x[:c] + '_' * (len(x) - c if len(x) > 0 else 0) for x in lst]))
    return ret

