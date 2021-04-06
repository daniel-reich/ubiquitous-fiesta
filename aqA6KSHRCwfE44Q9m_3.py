
def normalize(s):
    '''
    Returns sentence s manipulated as per instructions.
    '''
    return s[0].upper() + s[1:].lower() + '!' if s.isupper() else s

