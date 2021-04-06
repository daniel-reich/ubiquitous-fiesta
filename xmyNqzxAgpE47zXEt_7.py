
def is_alphabetically_sorted(sentence):
  s = ''.join(i for i in sentence.lower() if i.isalpha() or i == ' ')
  for word in s.split():
    if ''.join(sorted(word)) == word and len(word) > 2:
      return True
  return False

