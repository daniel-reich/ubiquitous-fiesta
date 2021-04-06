
def sigilize(wish):
    vowels=['a','o','i','e','u']
    nl=[]
    [nl.append(c) for c in wish.replace(' ','')[::-1] if not c in nl]
    return ''.join([c.upper() for c in nl[::-1] if not c.lower() in vowels])

