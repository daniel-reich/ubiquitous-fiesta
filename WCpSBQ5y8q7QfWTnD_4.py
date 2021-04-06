
def inflect(verb, person, number):
    
    prn = pronomi[person][number]
    base = verb[:-3]
    
    if verb[-3:] == "are":
        spec = verbi_spec[person][number][0]
    if verb[-3:] == "ere":
        spec = verbi_spec[person][number][1]    
    if verb[-3:] == "ire":
        spec = verbi_spec[person][number][2]    
    
    
    com = verbi_com[person][number]
    
    return (prn+" "+ base+spec+com)

