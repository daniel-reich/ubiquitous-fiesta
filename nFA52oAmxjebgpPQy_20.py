
def char_index(word, char):
  a=[b for b in range(len(word)) if word[b]==char]
  if a==[]:
    return None
  else:
    return [a[0],a[-1]]

