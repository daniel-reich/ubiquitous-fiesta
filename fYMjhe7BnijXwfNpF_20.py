
def middle(word):
  if len(word) == 1:
    return word
  return middle(word[1:-1])
​
def stmid(string):
  words = string.split(' ')
  output = ''
  for word in words:
    if len(word) % 2 == 0:
      output += word[0]
    else:
      output += middle(word)
  return output

