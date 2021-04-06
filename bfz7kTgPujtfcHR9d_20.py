
def x_pronounce(s):
  s = s.split(" ")
  for i in range(len(s)):
    if s[i] == "x": s[i] = 'ecks'
    if s[i].startswith("x"): s[i] = "z" + s[i][1:]
    if "x" in s[i]: s[i] = s[i].replace("x", "cks")
  return " ".join(s)

