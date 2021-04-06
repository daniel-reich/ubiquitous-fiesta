
def sentence(words):
  return ', '.join(add_pref(w) for w in words[:-1]).capitalize() + \
    ' and ' + add_pref(words[-1]) + '.'
  
def add_pref(w):
  return 'a' + 'n'*(w[0]in 'aeiou') + ' ' + w

