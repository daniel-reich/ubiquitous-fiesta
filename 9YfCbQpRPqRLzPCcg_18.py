
def will_hit(equation, position):
  equation += ' '
  num = []
  sign = 1
  a = '' 
  for i in range(len(equation)):
    if equation[i].isdigit():
      a += equation[i]
      if equation[i-1] == '-':
        sign = -1
    elif i == len(equation)-1:
      num.append(int(a)*sign)
    elif len(num) != 0:
      if equation[i] == '-' or equation[i] == '+':
        num.append(equation[i])
    else:
      if len(a) != 0:
        num.append(int(a)*sign)
        sign = 1
        a = ''
  if num[1] == '+':
    num [1] = 1
  else: 
    num[1] = -1
  x = position[0]
  y = num[0]*x + num[1]*num[2]
  return y == position[1]

