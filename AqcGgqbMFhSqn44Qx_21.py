
def tweet(txt):
  words = txt.split(' ')
  output = []
  for word in words:
    if word[0] in ('#@'):
      output.append(word)
  links = ' '.join(output)
  outstring = ''
  for i in links:
    if i.isalpha() or i in '#@ ':
      outstring += i
  return outstring

