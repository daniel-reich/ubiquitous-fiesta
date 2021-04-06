
def inflect(v, p, n):
    i =0 if v[-3] == 'a' else 1 if v[-3] == 'e' else 2
    return pronomi[p][n] + ' ' + v[:-3] + verbi_spec[p][n][i] + verbi_com[p][n]

