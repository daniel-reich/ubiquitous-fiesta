
def char_index(word, char):
  if char in word:
    return [word.find(char) , len(word)-word[::-1].find(char)-1]
  else:
    return None

