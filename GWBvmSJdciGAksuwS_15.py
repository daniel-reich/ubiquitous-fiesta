
def find_letters(word):
  lst = []
  for i in (word):
    if word.count(i) == 1:
      lst.append(i)
  return(lst)

