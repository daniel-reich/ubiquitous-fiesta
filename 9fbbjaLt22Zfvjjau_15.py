
def paul_cipher(txt):
  al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  ans,x = "",0
  for i in txt.upper():
    if i.isalpha():
      ans += al[(al.index(i)+x)%26]
      x = al.index(i)+1
    else: ans += i
  return ans

