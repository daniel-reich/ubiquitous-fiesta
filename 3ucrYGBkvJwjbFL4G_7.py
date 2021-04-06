
def reversible_inclusive_list(start, end, rev=None):
    if rev is None:
        if start > end:
            rev = True
            start, end = end, start
        else:
            rev = False       
    if start >= end:
        return [start]
    if rev:
        return reversible_inclusive_list(start+1, end, rev) + [start]
    else:
        return [start] + reversible_inclusive_list(start+1, end, rev)

