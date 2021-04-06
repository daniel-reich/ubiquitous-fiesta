
def sigilize(desire):
  string = desire.upper()[::-1]
  used = []
  sigil = ''
  for i in string:
    if i not in used and i not in ' AEIOU':
      used.append(i)
      sigil += i
  return sigil[::-1]

