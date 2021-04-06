
def inflect(verb, person, number):
    verb, end = verb[:-3], {"are":0, "ere":1, "ire":2}[verb[-3:]]
    verb += verbi_spec[person][number][end] + verbi_com[person][number]
    return "{} {}".format(pronomi[person][number], verb)

