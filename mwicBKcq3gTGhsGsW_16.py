
def make_word_riddle(s):
    
    part = list(s.lower().partition('in'))
    
    right_part = list(part[2])
    
    right_part.insert(1,part[0])
    
    return ''.join(right_part).upper()

