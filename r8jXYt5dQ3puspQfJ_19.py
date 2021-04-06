
def split(txt):
  vow = ''
  con = ''
  s= set("aeiou")
  for i in txt:
    if i in s:
      vow+=i
    else:
      con+=i
  return vow+con

