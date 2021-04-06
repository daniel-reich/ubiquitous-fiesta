
def conjugate(verb, n):
    d = {1: {'pronoun': 'Io', 'suffix': 'o'}, 
         2: {'pronoun': 'Tu', 'suffix': 'i'},
         3: {'pronoun': 'Egli', 'suffix': 'a'}, 
         4: {'pronoun': 'Noi', 'suffix': 'iamo'}, 
         5: {'pronoun': 'Voi', 'suffix': 'ate'},  
         6: {'pronoun': 'Essi', 'suffix': 'ano'}}
    
    root = verb[:-3]
    if root.endswith(('c', 'g')) and n in (2, 4):
        root += 'h'
    res = '{} {}{}'.format(d[n]['pronoun'], root, d[n]['suffix'])
    return res.replace('ii', 'i')

