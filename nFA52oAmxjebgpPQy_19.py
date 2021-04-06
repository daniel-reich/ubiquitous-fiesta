
def char_index(word, char):
  lst = []
  for i in range(len(word)):
    if word[i] == char:
      lst.append(i)
  if lst == []:
    return None
  else:
    return [lst[0],lst[len(lst)-1]]

