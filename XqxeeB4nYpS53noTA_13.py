
def construct_fence(p):
  p = p.replace("$","")
  p = p.replace(",","")
  a = int(1000000 / int(p))
  s = ""
  for i in range(a):
    s = s+'H'
  return s

