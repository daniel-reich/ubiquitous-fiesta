
def insert_whitespace(txt):
  ans=''
  for i in range(len(txt)-1):
    if txt[i].islower() and txt[i+1].isupper():
      ans+=txt[i]+' '
    else:
      ans+=txt[i]
  ans += txt[-1]
  return ans

