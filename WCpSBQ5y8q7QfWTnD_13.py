
def inflect(verb, person, number):
    gd = lambda dct: dct[person][number]
    vcat = 'aei'.find(verb[-3])
    return '{} {}{}{}'.format(gd(pronomi), verb[:-3], \
                              gd(verbi_spec)[vcat], gd(verbi_com))

