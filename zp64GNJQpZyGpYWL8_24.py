
def score_it(s):
  left = 0
  res = 0
  num = ''
  for i in range(len(s)):
    if s[i]=='(':
      left+=1
    elif s[i]==')':
      left-=1
    else:
      if s[i].isdigit():
        num+=s[i]
      if i+1<len(s) and s[i+1].isdigit() is False and num.isdigit():
        res+=left*int(num)
        num = ''
  return res

