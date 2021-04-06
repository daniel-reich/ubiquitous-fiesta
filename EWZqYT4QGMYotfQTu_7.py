
def tap_code(text):
  res = []
  if text[0] == ".":
    text = text.split()
    for i in range(0,len(text),2):
      c = chr((len(text[i])-1)*5+len(text[i+1])+97)
      if ord(c) < 108:
        c = chr(ord(c)-1)
      res += c
​
  else:
    for c in text:
      c = ord(c)-97
      if c == 10:
        c = 2
      elif c >= 11:
        c -= 1
      res += ["."]*(c//5+1) + [" "] + ["."]*(c%5+1) + [" "]
    res.pop()
​
  return "".join(res)

