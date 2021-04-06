
def x_pronounce(s):
    return ' '.join('ecks' if x=='x' else  'z'+x[1:] if x.startswith('x') else x.replace('x', 'cks') for x in s.split())

