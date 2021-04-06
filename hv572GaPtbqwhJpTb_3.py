
def elasticize(word):
  if len(word) < 3:
    return word
  output = ''
  for i in range((len(word)//2)):
    output += word[i] * (i+1)
  for i in range((len(word)//2),len(word)):
    output += word[i] * ((len(word)-i))
  return output

