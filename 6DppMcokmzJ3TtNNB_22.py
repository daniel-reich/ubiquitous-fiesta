
def true_alphabetic(txt):
  words = txt.split(' ')
  str = ''.join(sorted(''.join(words)))
  arr = []
  i = 0
  for w in words:
    length = len(w)
    arr.append(str[i:(i+length)])
    i += length
  return ' '.join(arr)

