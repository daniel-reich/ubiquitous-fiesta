
def map_letters(word):
  dic = {}
  for i,letter in enumerate(word):
    if letter not in dic:
      dic[letter] = []
    dic[letter].append(i)
  return dic

