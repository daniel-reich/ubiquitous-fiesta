
def inflect(verb, person, number):
    end = {'are': 0, 'ere': 1, 'ire': 2}
    ver = verb[:-3]+verbi_spec[person][number][end[verb[-3:]]]+verbi_com[person][number]
    return pronomi[person][number] + ' ' + ver

