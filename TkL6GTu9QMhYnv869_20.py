
def add_ending(lst, ending):
  lst2 = []
  for word in lst:
    word = word + ending
    lst2.append(word)
  return lst2

