
def find_letters(word):
  list = []
  counter = 0
  for i in word:
    counter = word.count(i)
    if counter == 1:
      list.append(i)
  return list

