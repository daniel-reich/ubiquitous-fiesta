
def score_it(s):
  num_o=0
  num_c=0
  num=''
  res=0
  for i in range(len(s)-1):
    if s[i]=='(':
      num_o+=1
    elif s[i]==')':
      num_c+=1
    if s[i].isdigit():
      num+=s[i]
      if s[i+1]=='(' or s[i+1]==')' or s[i+1].isalpha():
        res+=(num_o-num_c)*int(num)
        num=''    
  return res

