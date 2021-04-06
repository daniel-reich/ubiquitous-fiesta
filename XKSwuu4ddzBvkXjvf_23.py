
def sentence_primeness(sentence):
  words = [''.join(i for i in word if i.isalnum()) for word in sentence.split()]
  word_value = [sum([ord(i.lower()) - 96 if i.isalpha() else int(i) for i in word]) for word in words]
  if is_prime(sum(word_value)):
    return 'Prime Sentence'
  for num in word_value:
    if is_prime(sum(word_value) - num):
      return 'Almost Prime Sentence ({})'.format(words[word_value.index(num)])
  return 'Composite Sentence'
​
def is_prime(n):
  if n > 1:
    for i in range(2,n):
      if n % i == 0:
        return False
    return True
  else:
    return False

