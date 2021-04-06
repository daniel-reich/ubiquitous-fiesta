
def is_authentic_skewer(mix):
    '''
    Returns True if mix is a consistent set of vowel - space(s) - consonants
    as per the instructions
    '''
    CONSONANTS = set('BCDFGHJKLMNPQRSTVWXYZ')
    VOWELS = set('AEIOU')
    
    size = len(mix)
    pattern = ''.join(['C' if c in CONSONANTS else 'V' if c in VOWELS else c
                       for c in mix])  # pattern of consonants, vowels etc
    if size < 5 or pattern[0] != 'C' or pattern[1] != '-':
        return False
    
    count = 0
    i = 1
    while pattern[i] == '-':
        count += 1  # size of 1st skewer space
        i += 1
        
    num = size // (2 * (count + 1))  # number of c - v -  sets expected
    legit_set = 'C' + '-' * count + 'V' + '-' * count
    
    return pattern == legit_set * num + 'C'

