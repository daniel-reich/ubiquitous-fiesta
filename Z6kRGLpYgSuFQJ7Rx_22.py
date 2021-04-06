
def find_longest(sentence):
  
  longest_word = ''
  biggest_size = 0
  
  
  words = sentence.split()
  print(words)
  for word in words:
    if '\'' in word:
      word = ''.join([i for i in list(word[:word.index('\'')])])
    if '.' in word:
      word = word.replace('.', '')
    if len(word) > biggest_size:
      longest_word = word
      biggest_size = len(word)
  
  return longest_word.lower()

