
def replace(txt, r):
  str=""
  for i in txt:
    if ord(i)>=ord(r[0]) and ord(i)<=ord(r[-1]):
      str+="#"
    else:
      str+=i
  return str

