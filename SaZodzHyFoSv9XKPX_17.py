
def domino_chain(dominos):
  ans =''
  flag = 1
  
  for i in dominos:
    if i == '/' or i == ' ':
      flag = 0
      
    if flag:
      ans += '/'
    else:
      ans += i
  
  return ans

