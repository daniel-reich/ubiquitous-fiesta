
def babbage(n):
  c,ans = 2,0
  while True:
    if str(c**2)[-(len(str(n))):] == str(n):
      ans=c
      break
    c+=1
  if n==269696:
    if ans==99736:
      return 'Babbage was correct!'
    else:
      return 'Babbage was incorrect!'
  return ans

