
def cap_space(txt):
  temp = ''
  for i in txt:
    if i == i.lower():
      temp += i
    else:
      temp += ' ' + i.lower()
  return temp

