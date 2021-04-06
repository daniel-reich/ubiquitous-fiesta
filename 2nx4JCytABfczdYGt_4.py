
def conjugate(verb, pronoun):
    pronoun_dict = {1: 'Io',
               2:'Tu',
               3: 'Egli',
               4: 'Noi',
               5: 'Voi',
               6: 'Essei'}
​
    suffix_dict = {1: 'o',
               2:'i',
               3: 'a',
               4: 'iamo',
               5: 'ate',
               6: 'ano'}
    
    root = verb[:-3]
    last_letter = verb[:-3][-1]
    
    if pronoun == 2 or pronoun == 4:
        if last_letter == "c" or last_letter == "g":
            return pronoun_dict[pronoun]+ " " + root + 'h' + suffix_dict[pronoun]
        elif last_letter == "i":
            return pronoun_dict[pronoun]+ " " + root[:-1] + suffix_dict[pronoun]
            
        else:
            return pronoun_dict[pronoun]+ " " + root + suffix_dict[pronoun]
    else:
        return pronoun_dict[pronoun]+ " " + root + suffix_dict[pronoun]

