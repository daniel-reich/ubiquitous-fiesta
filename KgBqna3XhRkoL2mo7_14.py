
def decrypt(s):
  d = dict({str(i):chr(i+96) for i in range(1,11)},
      **{str(i)+'#':chr(i+96) for i in range(10,27)})
  i = 0
  ans =''
  
  while i <len(s):
    if i < len(s)-2 and s[i+2] == '#':  
      ans+=d[s[i:i+3]]
      i+= 3
    else:
      ans+= d[s[i]]
      i+=1
  
  return ans

