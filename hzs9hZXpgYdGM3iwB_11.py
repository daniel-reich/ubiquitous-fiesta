
def alternating_caps(txt):
  s=list(txt.replace(" ",""))
  for i in range(len(s)):
    if i%2==0:
      s[i]=s[i].upper()
    else: s[i]=s[i].lower()
  x=[index for index,val in enumerate(txt) if val==" "]
  for num in x:
    s.insert(num," ")
  return "".join(s)

