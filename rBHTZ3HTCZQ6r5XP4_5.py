
def expanded_form(n):
  a,b = str(n).split('.')
  a = ' + '.join([str((10**(len(a)-i-1))*int(j)) for i,j in enumerate(a) if str((10**(len(a)-i-1))*int(j))!='0'])
  b = ' + '.join([str(int(j))+'/'+str('1'+'0'*(i+1)) for i,j in enumerate(b) if str(int(j))!='0'])
  return a +' + ' + b if a and b else b if not a else a

