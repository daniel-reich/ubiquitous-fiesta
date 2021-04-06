
def partially_hide(phrase):
  temp = phrase.split(' ')
  result = ''
  for i in range(len(temp)):
    j = len(temp[i])-2
    result += temp[i][0]
    result += '-'*j
    result += temp[i][-1]
    result += ' '
  
  return result[:-1]

