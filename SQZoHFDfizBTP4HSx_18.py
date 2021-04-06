
def missing_alphabets(txt):
  
  full_alph = 'abcdefghijklmnopqrstuvwxyz'
  
  l8r_count = {}
  
  for l8r in full_alph:
    l8r_count[l8r] = txt.count(l8r)
  
  alph_nums = max(list(l8r_count.values()))
  
  tr = ''
  
  for l8r in full_alph:
    tr += (l8r * (alph_nums - l8r_count[l8r]))
  
  return tr

