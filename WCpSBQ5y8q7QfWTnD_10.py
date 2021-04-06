
def inflect(verb, person, number):
    ending = ["are", "ere", "ire"]
    a = pronomi[person][number] 
    b = verbi_spec[person][number][ending.index(verb[-3:])]
    c = verbi_com[person][number]
    return '{} {}{}{}'.format(a,verb[:-3],b,c)

