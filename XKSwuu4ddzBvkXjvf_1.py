
def sentence_primeness(sentence):
  words = ''.join(ch for ch in sentence if ch.isalnum() or ch == ' ').split()
  values = [get_word_value(w) for w in words]
  
  if is_prime(sum(values)):
    return 'Prime Sentence'
  else:
    for i in range(len(values)):
      if is_prime(sum(values[:i]+values[i+1:])):
        return 'Almost Prime Sentence ({})'.format(words[i])
  return 'Composite Sentence'
​
def get_word_value(word):
  v = ' abcdefghijklmnopqrstuvwxyz'
  res = 0
  for ch in word:
    if ch.isdigit():
      res += int(ch)
    else:
      res += v.find(ch.lower())
  return res
​
def is_prime(n):
  return not any(not n%i for i in range(2,int(n**0.5)+1))

