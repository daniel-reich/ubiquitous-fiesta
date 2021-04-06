
def conjugate(verb, pronoun):
  p = {1:'Io ',2:'Tu ',3:'Egli ',4:'Noi ',5:'Voi ',6:'Essi '}
  s = {1:'o',2:'i',3:'a',4:'iamo',5:'ate',6:'ano'}
  verb = verb[:-3]
  if verb.endswith('i') and s[pronoun].startswith('i'):
    return p[pronoun]+verb[:-1]+s[pronoun]
  elif verb.endswith('c') or verb.endswith('g'):
    return p[pronoun]+verb+'h'+s[pronoun]
  else:
    return p[pronoun]+verb+s[pronoun]

