
def makeBox(n):
  arr = []
  strr = ""
  if n == 1:
      arr.insert(0,"#")
  else:
      arr.insert(0,"#"*n)
      for i in range(1,n-1):
          strr = ""
          strr = strr + "#" + (" "*(n-2)) + "#"
          arr.insert(i,strr)
      arr.insert(n,"#"*n)
  return arr

