
def pad(message):
    s = (message + ' l' + 'ol'*70)[:140]
    if s.endswith('o'):
        s = s.replace(' ', '', 1) + 'l'
    return s

