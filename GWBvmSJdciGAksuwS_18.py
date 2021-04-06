
def find_letters(word):
  f = []
  for i in word:
    if word.count(i)==1:
      f.append(i)
  return f

