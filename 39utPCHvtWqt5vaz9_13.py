
def direction(lst):
  dst = []
  for word in lst:
    word = word.replace('E', 'W').replace('A', 'E').replace('e', 'w').replace('a', 'e')
    dst.append(word)
  return dst

