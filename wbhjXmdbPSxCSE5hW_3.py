
def sigilize(desire):
  x = ''.join(char for char in desire if char.lower() not in 'aeiou')
  x = x.replace(" ","").upper()
  bla = []
  for i in x[::-1]:
    if i not in bla:
      bla.append(i)
  return "".join(a for a in bla[::-1])

