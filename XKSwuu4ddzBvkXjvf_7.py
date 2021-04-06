
import re
​
def is_prime(n):
  return n > 1 and all(n % x != 0 for x in range(2, int(n**.5) + 1))
​
def value(w):
  return sum(int(x) if x.isdigit() else ord(x) - 96 for x in w.lower())
​
def sentence_primeness(sentence):
  sen = re.findall(r'\w+', sentence)
  full = sum(value(w) for w in sen)
  if is_prime(full):
    return 'Prime Sentence'
  else: 
    for w in sen:
      if is_prime(full - value(w)):
        return 'Almost Prime Sentence ({})'.format(w)
    return 'Composite Sentence'

