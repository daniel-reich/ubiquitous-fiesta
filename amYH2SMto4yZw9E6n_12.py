
def validate(s):
  numbers={str(i) for i in range(10)}
  if '  ' in s: return False
  if s.isdigit():
    if s[0]=='1': s=s[1:]
    return len(s)==10
  if s[0]=='+':
    if s[1]!='1': return False
    s=s[1:]
  if s[0]=='1': s=s[2:]
  if s[0]=='(':
    if s[4:6]!=') ' or s[-5]!='-': return False
    s=s[1:].replace(')','').replace('-',' ')
  delim = {'.', ')', '(', '-', '/', ' '}
  if len(set(s)-numbers-delim): return False
  if len(set(s)-numbers)!=1: return False
  for i in '-/.':
    s=s.replace(i,' ')
  s=s.split()
  return len(s[0])==len(s[1])==len(s[2])-1

