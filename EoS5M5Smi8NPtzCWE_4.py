
def secret(text):
  st = text.split("*")
  n = int(st[1])
  r = ""
  for i in range(n):
    r += "<{0}></{0}>".format(st[0])
  return r

