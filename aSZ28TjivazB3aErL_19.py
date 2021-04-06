
def letters_only(s):
  x = list(str(s))
  w = []
  for i in x:
    if i not in "qwertyuiopasdfghjklzxcvbnm ":
      w.append("False")
    else:
      w.append("True")
  if "False" in w or s=='':
    return False
  else:
    return True

