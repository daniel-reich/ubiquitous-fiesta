
def char_at_pos(r, s):
  if isinstance(r, list):
    arr = list()
    if s == "odd":
      for i in range(len(r)):
        if (i+1) % 2 != 0:
          arr.append(r[i])
    elif s == "even":
      for i in range(len(r)):
        if (i+1) % 2 == 0:
          arr.append(r[i])
    return arr
  else:
    stri = ' '
    if s == "odd":
      for i in range(len(r)):
        if (i+1) % 2 != 0:
          stri += r[i]
    elif s == "even":
      for i in range(len(r)):
        if (i+1) % 2 == 0:
          stri += r[i]
    return stri.strip()

