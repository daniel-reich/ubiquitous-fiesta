
def decrypt(s):
  s = list(s)
  while any(i == "#" for i in s):
    tag = s.index("#")
    s[tag - 2:tag] = ["".join(s[tag - 2:tag])]
    del s[tag - 1]
  return "".join(chr(96 + int(i)) for i in s)

