
def dashed(txt):
    
    return ''.join(['-{}-'.format(i) if i in 'AEIOUaeiou' else i for i in txt])

