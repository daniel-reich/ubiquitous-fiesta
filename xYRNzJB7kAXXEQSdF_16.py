
def wiggle_string(s):
  lst = [s, ]
  for i in range(1, len(s)+1):
    lst.append(" "*i + s)
  return lst + lst[-2::-1]

