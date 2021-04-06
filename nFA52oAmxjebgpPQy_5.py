
def char_index(word, char):
  if char not in word:
    return None
  elif word.count(char) == 1:
    return [word.index(char),word.index(char)]
  else:
    temp = []
    for i in range(len(word)):
      if word[i] == char:
        temp.append(i)
    return [temp[0],temp[-1]]

