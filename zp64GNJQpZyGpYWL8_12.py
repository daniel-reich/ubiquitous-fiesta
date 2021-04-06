
def score_it(s):
    tot = 0
    lvl = 0
    nbr = ''
    for x in s:
        if x == '(':
            if nbr:
                tot += lvl*int(nbr)
                nbr = ''
            lvl += 1
        elif x == ')':
            if nbr:
                tot += lvl*int(nbr)
                nbr = ''
            lvl -= 1
        elif x.isdigit():
            nbr += x
    return tot

