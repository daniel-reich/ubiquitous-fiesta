
def char_index(word, char):
  lst = []
  word = list(word)
  for i in range(len(word)):
    if word[i] == char:
      lst.append(i)
  if len(lst) == 0:
    return None
  return [lst[0],lst[-1]]

