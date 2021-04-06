
def new_word(word):
  word = ''.join(list(filter(lambda x: x.isalpha() or x.isdigit(),word)))
  return word
​
def value(char):
  if char.isdigit():
    return int(char)
  elif char.isupper():
    return ord(char) - 64
  else:
    return ord(char) - 96
    
def isPrime(n):
  if n == 1:
    return False
  elif n == 2:
    return True
  else:
    return len(list(filter(lambda x: n % x == 0,range(2,n)))) == 0
def sum_chars(word):
  return sum(list(map(lambda x: value(x),new_word(word))))
  
def sentence_primeness(sentence):
  words = sentence.split(" ")
  total = sum(list(map(lambda x: sum_chars(x),words)))
  if isPrime(total):
    return "Prime Sentence"
  else:
    new_totals = list(filter(lambda x: isPrime(total - sum_chars(words[x])),range(0,len(words))))
    if len(new_totals) > 0:
      return 'Almost Prime Sentence ({})'.format(new_word(words[new_totals[0]]))
    else:
      return "Composite Sentence"

