
def x_pronounce(sentence):
  a = ""
  k = ""
  sentence += " "
  for letter in sentence:
    if letter != " ":
      a += letter
    else:
      if a == "x":
        k += "ecks" +" "
      elif a[0] == "x":
        k += ("z" + a[1:]) + " "
      elif a.count("x") > 0:
        k += (a[:a.index("x")] + "cks" + a[a.index("x")+1:]) + " "
      else:
        k += (a + " ")
      a = ""
  return k[:-1]

