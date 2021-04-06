
def wiggle_string(s):
  lst = []
  for i in range(0, len(s)):
    lst.append("{}{}".format(" "*i, s))
  for i in range(len(s), -1, -1):
    lst.append("{}{}".format(" "*i, s))
  return lst

