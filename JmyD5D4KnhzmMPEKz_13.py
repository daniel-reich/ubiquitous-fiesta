
def constraint(txt):
  def is_panagram(words):
    l8rs = ''
    a = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    
    for word in words:
      l8rs += word
    
    for l8r in a:
      if l8r not in l8rs:
        return False
    return True
  def is_heterogram(words):
    l8rs = ''
    
    for word in words:
      l8rs += word
    
    s = set(l8rs)
    
    return len(l8rs) == len(list(s))
  def is_tautogram(words):
    
    imp_l8rs = []
    
    for word in words:
      imp_l8rs.append(word[0])
    
    s = list(set(imp_l8rs))
    
    return len(s) == 1
  def is_transgram(words):
    
    sets = []
    
    for word in words:
      sets.append(list(set(word)))
    
    for st in sets:
      for l8r in st:
        c = 0
        for s in sets:
          if l8r in s:
            c += 1
        if c == len(sets):
          return True
    return False
  
  words = txt.lower().split()
  
  panagram = is_panagram(words)
  heterogram = is_heterogram(words)
  tautogram = is_tautogram(words)
  transgram = is_transgram(words)
  
  if panagram == True:
    return 'Pangram'
  elif heterogram == True:
    return 'Heterogram'
  elif tautogram == True:
    return 'Tautogram'
  elif transgram == True:
    return 'Transgram'
  else:
    return 'Sentence'

