
def min_palindrome_steps(txt):
  if txt==txt[::-1]:  return 0
  l = [txt+txt[::-1][x:] for x in range(len(txt)-1,-1,-1)]
  p = [l[x] for x in range(len(l)) if l[x]==l[x][::-1]]
  return len(p[0])-len(txt)

