
def word_builder(ltr, pos):
  result = []
  for i in pos:
    a = ltr[i]
    result.append(a)
  return ''.join(result)

