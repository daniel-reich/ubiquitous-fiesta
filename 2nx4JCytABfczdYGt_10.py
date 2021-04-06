
def conjugate(verb, pronoun):
  pr = ['Io', 'Tu', 'Egli', 'Noi', 'Voi', 'Essi']
  suf = ['o', 'i', 'a', 'iamo', 'ate', 'ano']
  root = verb[:-3]
  suffix = suf[pronoun-1]
  
  if root.endswith('c') or root.endswith('g'):
    suffix = 'h' + suffix
  elif root.endswith('i'):
    if suffix.startswith('i'):
      suffix = suffix[1:]
  return pr[pronoun-1] + ' ' + root + suffix

