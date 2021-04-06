
def bifid(text):
  p = [['A','B','C','D','E'],
    ['F','G','H','I','K'],
    ['L','M','N','O','P'],
    ['Q','R','S','T','U'],
    ['V','W','X','Y','Z']]
  cipher = ' ' not in text
  text = [i.upper() for i in text if i.upper() in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
  numbers = [char_to_number(i,p) for i in text]
  if not cipher:
    top,bottom = [i[0] for i in numbers],[i[1] for i in numbers]
    new_num = top + bottom
    new_num = [new_num[i:i+2] for i in range(0,len(new_num),2)]
  else:
    numbers = [i for x in numbers for i in x]
    top = numbers[:len(numbers)//2]
    bottom = numbers[len(numbers)//2:]
    new_num = [[top[i]]+[bottom[i]] for i in range(len(top))]
  ans = [p[i[0]][i[1]].lower() for i in new_num]
  return ''.join(ans)
  
def char_to_number(ch,p):
  if ch == 'J':
    return [1,3]
  for i in range(len(p)):
    if ch in p[i]:
      return [i,p[i].index(ch)]

