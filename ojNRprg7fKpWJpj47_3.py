
def shift_sentence(s):
    '''
    Shifts the 1st letter of each word in sentence s to the next word cyclically to
    the right as above then returns the altered sentence.
    '''
    s = s.split()
    
    return ' '.join([s[i].replace(s[i][0], s[(i-1)%len(s)][0], 1) for i in range(len(s))])

