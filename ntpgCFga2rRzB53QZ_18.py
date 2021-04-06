
def staircase(n):
  
  def recur_pos(num):
    if num > 0:
      return ''.join('_'*(num - 1) + '#'*(n - num + 1) + '\n' + str(recur_pos(num - 1)))
    else:
      return ''
      
  def recur_neg(num):
    if num > 0:
      return ''.join(str(recur_neg(num - 1)) + '_'*(num - 1) + '#'*((-1)*n - num + 1) + '\n')
    else:
      return ''
  
  if n > 0:
    return recur_pos(n)[:-1]
  else:
    return recur_neg((-1)*n)[:-1]

