
import string 
​
ans = []
​
def Solve(s, comb): 
  if len(s) == 0:
    ans.append(comb)
    return
  
  sub = ''  
  i = 0
  
  while i < len(s):
    if s[i] == '[' or s[i] == ']':      
      break
    if s[i].isalpha() or s[i].isdigit() or s[i] in string.punctuation + ' ':
      sub += s[i]           
    i += 1
  s = s[i + 1:]
  
  if '|' in sub:
    for i in sub.split('|'):
      Solve(s, comb + i)
  else:
    Solve(s, comb + sub)
  
    
      
    
    
def unravel(s):
  global ans
  ans = []
  
  Solve(s, '')
  mn = min(len(x) for x in ans)
  
  print(s)
  print(ans)
  
  return sorted(ans)

