
def worded_math(equ):
  lst = []
  equ = equ.lower()
  a = equ.split(" ")
  for i in a:
    if i == 'one':
      lst.append('1')
    elif i == 'zero':
      lst.append('0')
    elif i == 'minus':
      lst.append('-')
    elif i == 'plus':
      lst.append('+')
  lst = ' '.join(lst)
  if eval(lst) == 0:
    return 'Zero'
  elif eval(lst) == 1:
    return 'One'
  else:
    return 'Two'

