
def replace_the(txt):
  s=txt.split(' ')
  for i in range(1,len(s)):
    if s[i-1]=='the' and s[i][0] in ['a','e','i','o','u']:
      s[i-1]='an'
    elif s[i-1]=='the' and s[i][0] not in ['a','e','i','o','u']:
      s[i-1]='a'
    else: 
      pass
  return ' '.join(s)

