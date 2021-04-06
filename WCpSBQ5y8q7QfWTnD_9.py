
def inflect(verb, person, number):
    pos = {'are':0, 'ere':1, 'ire':2}
    base = verb[:len(verb)-3]
    end = verb[len(verb)-3:]
    p = pronomi[person][number]
    vs = verbi_spec[person][number][pos[end]]
    vc = verbi_com[person][number]
    return p + ' ' + base + vs + vc

