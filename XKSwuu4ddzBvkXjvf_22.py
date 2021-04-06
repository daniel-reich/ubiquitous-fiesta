
def prime(num):
  d = 3
  if num == 1 or num == 2:
    return True
  if num % 2 == 0:
    return False
  while d*d <= num:
    if num % d == 0:
      return False
    d += 2
  return True
​
def sentence_primeness(sentence):
  s = ''
  for c in sentence:
    if (ord(c) >= 65 and ord(c) <= 91) or (ord(c) >= 97 and ord(c) <= 122) or (ord(c) >= 48 and ord(c) <= 57) or ord(c) == 32:
      s += c
  
  
  ls = s.split()
  ls_val = []
  
  for item in ls:
    val = 0
    for c in item:
      if ord(c) <= 57:
        val += ord(c) - 48
      elif ord(c) <= 91:
        val += ord(c) - 64
      elif ord(c) <= 122:
        val += ord(c) - 96
    ls_val.append(val)
  
  num_prime = 0
  to_rem = ''
  
  
  
  tot = sum(ls_val)
  if prime(tot):
    return 'Prime Sentence'
  else:
    for i in range(len(ls)):
      if prime(tot - ls_val[i]):
        to_rem = ls[i]
        return 'Almost Prime Sentence (' + to_rem + ')'
    return 'Composite Sentence'

