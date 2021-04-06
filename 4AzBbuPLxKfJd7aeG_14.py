
def encrypt(key, message):
  x=1
  S=""
  for letter in key:
    S=S+letter
    if x%2==0:
      S=S+" "
    x=x+1
​
  x=0
  y=0
  result=""
  for letter in message:
    if letter in key and x+1<=len(message):
      y=S.index(letter)
      if S[y]==" ":
        y=y+1
      if (y-1)%3!=2:
        result=result+S[y-1]
      else:
        result=result+S[y+1]
    else:
      result=result+message[x]
    x=x+1
  return result

