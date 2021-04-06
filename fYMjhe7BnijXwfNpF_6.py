
def stmid(string):
  lst = string.split()
  txt = ''
  for i in lst:
    if len(i) % 2:
      txt += i[(len(i) // 2)]
    else:
      txt += i[0]
  return txt

