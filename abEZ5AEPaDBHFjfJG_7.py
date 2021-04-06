
def formula(txt):
  t=''
  if txt=='':
    return None
  for i in txt:
    if i=='=':
      t+='=='
    elif i=='a':
      t+='4'
    else:
      t+=i
  return eval(t)

