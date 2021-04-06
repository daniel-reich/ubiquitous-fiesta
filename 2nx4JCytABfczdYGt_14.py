
def conjugate(verb, pronoun):
    root = verb[:-3]
    pron = ['Io ', 'Tu ', 'Egli ', 'Noi ', 'Voi ', 'Essi ']
    suf = ['o', 'i', 'a','iamo', 'ate', 'ano']
    if (root.endswith('c') or root.endswith('g')) and (pronoun==2 or pronoun==4):
        return pron[pronoun-1]+root+'h'+suf[pronoun-1]
    elif root.endswith('i') and (pronoun==2 or pronoun==4):  
        return pron[pronoun-1]+root+suf[pronoun-1][1:]    
    return pron[pronoun-1]+root+suf[pronoun-1]

