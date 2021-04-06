
def calc(s):
  a = "".join(str(ord(i)) for i in s)
  return a.count("7")*6

