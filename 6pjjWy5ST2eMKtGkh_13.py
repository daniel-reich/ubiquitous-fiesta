
def replace(txt, r):
  lister = r.split('-')
  output = ''
  for letters in txt:
    if letters < lister[0] or letters > lister[1]:
      output += letters
    else:
      output += '#'
  return output

