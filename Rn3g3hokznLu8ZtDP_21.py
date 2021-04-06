
def increment_string(txt):
  if txt[-1].isdigit():
    i = -1
    while txt[i] == "9":
      i -= 1
    return txt[:i] + str(int(txt[i:]) + 1)
  return txt + "1"

