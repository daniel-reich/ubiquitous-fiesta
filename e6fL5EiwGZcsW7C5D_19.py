
def alph_num(txt):
  str1 = ""
  for x in range(len(txt)):
    if x != len(txt) - 1:
      str1 += str(ord(txt[x])-65) + " "
    else:
      str1 += str(ord(txt[x])-65)
  return str1

