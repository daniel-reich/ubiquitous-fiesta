
def partially_hide(phrase):
  res = []
  for word in phrase.split():
    res.append(word[0] + ('-'*(len(word)-2)) + word[-1] )
  return ' '.join(res)

