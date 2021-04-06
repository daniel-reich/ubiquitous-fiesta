
def separate_numbers(s):
  l=len(s)
  #print(s)
  for a in range(1,l//2):
    x=int(s[0:a])
    out=""
    while len(out)<l:
      out+=str(x)
      x+=1
    #print(out)
    if out==s: return "YES "+ s[0:a]
  return "NO"

