
def pyramidal_string(string, _type):
  a = 0
  b = 1
  if _type == "REV":
    string = string[::-1]
  lst = []
  while a < len(string):
    temp = []
    for i in range(b):
      if a >= len(string):
        return 'Error!'
      else:
        temp.append(string[a])
      a += 1
    if _type == "REV":
      lst.append(' '.join(temp[::-1]))
    else:
      lst.append(' '.join(temp))
    b += 1
  return lst if _type == "REG" else lst[::-1]

