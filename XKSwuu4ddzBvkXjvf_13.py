
def sentence_primeness(txt):
  txt = ''.join(ch for ch in txt if ch.isalnum() or ch == ' ')
  words = txt.split()
  
  get_value = lambda x: sum(ord(ch.lower())-96 if ch.isalpha() else int(ch) for ch in x if ch.isalnum())
  
  if is_prime(get_value(txt)):
    return 'Prime Sentence'
    
  for w in words:
    if is_prime(get_value(txt) - get_value(w)):
      return 'Almost Prime Sentence ({})'.format(w)
      
  return 'Composite Sentence'
  
def is_prime(n):
  return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

