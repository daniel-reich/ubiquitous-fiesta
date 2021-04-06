
def can_build(txt1, txt2):
  txt2 = list(txt2)
​
  for char in txt1:
    if (char != " "):
      try:
        txt2.remove(char)
​
      except:
        return False
​
  return True

