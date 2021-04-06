
def coloured_triangle(row):
  s = str(row)
  while len(s) != 1:
    temp = ""
    for i in range(len(s)-1):
      if s[i] == s[i+1]:
        temp += s[i]
      elif ord(s[i]) + ord(s[i+1]) == 137:
        temp += "R"
      elif ord(s[i]) + ord(s[i+1]) == 153:
        temp += "B"
      else:
        temp += "G"
    s = temp
  return s

