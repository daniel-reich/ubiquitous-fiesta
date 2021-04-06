
def babbage(n):
  num = 0
  s = str(n)
  l = len(s)
  while True:
    p = num**2
    if s == str(p)[l*-1:]:
      break
    num += 1
  if n == 269696 and num == 99736:
    return "Babbage was correct!"
  elif n == 269696 and num != 99736:
    return "Babbage was incorrect!"
  else : return num

