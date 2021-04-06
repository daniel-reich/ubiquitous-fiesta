
def is_slidey(n):
  s= str(n)
  print(n)
  for i in range(1,len(s)):
    if int(s[i]) != int(s[i-1])-1 and int(s[i]) != int(s[i-1])+1:
      return False
  else:
    return True

