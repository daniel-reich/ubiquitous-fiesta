
def inflect(verb, person, number):
    idx_dct= {'a':0,'e':1,'i':2}
    return pronomi[person][number] + ' ' + verb[:-3]+verbi_spec[person][number][idx_dct[verb[-3]]] + verbi_com[person][number]

