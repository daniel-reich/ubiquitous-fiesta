
def ing_extractor(string):
  a="abcdefghijklmnopqrstuvwxyz"
  b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  f=[]
  v=""
  s=string.split()
  for d in range(len(s)):
    for r in range(len(s[d])):
      if s[d][r] in a or s[d][r] in b or s[d][r]=="*":
        v=v+s[d][r]
    s[d]=v
    v=""
  for e in s:
    if e[len(e)-3:len(e)].lower()=="ing":
      if "o" in e[0:len(e)-3].lower() or "a" in e[0:len(e)-3].lower() or "e" in e[0:len(e)-3].lower() or "i" in e[0:len(e)-3].lower() or "u" in e[0:len(e)-3].lower() or "*" in e[0:len(e)-3].lower():
        f.append(e)
  return f

