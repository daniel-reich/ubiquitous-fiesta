
def alternate_pos_neg(l):
  
  if 0 in l:
    return False
  else:
    constructor = ['>0','<0'] if l[0] > 0 else ['<0','>0']
​
    for i in range(len(l)):
      if not eval('{}{}'.format(str(l[i]),constructor[i%2])) :
        return False
​
    return True

