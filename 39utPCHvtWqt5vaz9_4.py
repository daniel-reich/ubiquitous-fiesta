
def direction(lst):
  output = []
  for i in lst:
    word = ''
    for j in i:
      if j == 'e':
        word += 'w'
      elif j == 'E':
        word += 'W'
      elif j == 'a':
        word += 'e'
      elif j == 'A':
        word += 'E'
      else:
        word += j
    output.append(word)
  return output

