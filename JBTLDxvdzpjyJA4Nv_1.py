
def super_reduced_string(t):
  while 1:
    for x,y in zip(t,t[1:]):
      if x==y:t=t.replace(x+y,'',1);break
    else:return t or'Empty String'

