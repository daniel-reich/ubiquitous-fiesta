
def reverse(txt):
  if txt == '':
    return txt
  else:
    print(reverse(txt[1:]) + txt[0])
    return reverse(txt[1:]) + txt[0]

