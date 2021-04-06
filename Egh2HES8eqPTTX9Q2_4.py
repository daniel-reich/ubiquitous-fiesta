
def rolling_cipher(txt, n):
  return "".join(alphaSwap(c,n%26) for c in txt)
​
def alphaSwap(c,add):
  cur = ord(c)-ord("a")+1
  if cur+add<=26:
    return(chr(ord(c)+add))
  add = (cur+add)%26
  return(chr(ord("a")+add-1))

