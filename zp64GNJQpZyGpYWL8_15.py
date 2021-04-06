
def score_it(s):
  ret = 0
  level = 0
  num = ''
  for i in s:
    if i == '(':
      if num!='':
        ret+=int(num)*level
        num=''
      level+=1
    elif i == ')':
      if num!='':
        ret+=int(num)*level
        num=''
      level-=1
    elif i.isdigit():
      num+=i
  return ret

