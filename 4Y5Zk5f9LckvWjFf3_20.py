
def special_reverse(s, c):
  b = ""
  a = s.split()
  d = ""
  for i in a:
    if(i[0] == c):
      d = i[::-1]
      b += d
    else:
      b += i
    b += " "
  return b[0:len(b)-1]

