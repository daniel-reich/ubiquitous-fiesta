
def sentence_primeness(sentence): 
  sentence = ''.join([i for i in sentence if i.isalnum() or i == ' ']).split()
  s = [val(i.lower()) for i in sentence]
  if is_prime(sum(s)):
    return "Prime Sentence"
  else:
    for i in range(len(s)):
      if is_prime(sum(s)-s[i]):
        return "Almost Prime Sentence (" + sentence[i] +")"
    return "Composite Sentence"
  
def is_prime(n):
  for i in range(2,n):
    if n%i == 0:
      return False
  return n != 1
​
def val(s):
  a = ' abcdefghijklmnopqrstuvwxyz'
  x = 0
  for i in s:
    if i.isalpha():
      x += a.index(i)
    else:
      x += int(i)
  return x

