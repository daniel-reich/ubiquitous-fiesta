
def validate_spelling(txt):
  
  raw = txt.split()
  
  word = raw[-1]
  l8rs = []
  
  for l8r in raw[:-1]:
    for item in l8r:
      if item != '.':
        l8rs.append(item)
  
  word = list(word.upper().strip('?').strip('!').strip('.')) 
  
  return word == l8rs

