
def ascii_capitalize(txt):
  cuv = ''
  for i in range(len(txt)):
    if txt[i] == ' ':
      cuv = cuv + ' '
    elif (ord(txt[i]) < ord('a') or ord(txt[i]) > ord('z')) and (ord(txt[i]) < ord('A') or ord(txt[i]) > ord('Z')):
      cuv = cuv + txt[i]
    elif ord(txt[i]) % 2 == 1 and ord(txt[i]) < ord('a'):
      cuv = cuv + chr(ord(txt[i]) + 32)
    elif ord(txt[i]) % 2 == 0 and ord(txt[i]) > ord('Z'):
      cuv = cuv + chr(ord(txt[i]) - 32)
    else:
      cuv = cuv + txt[i]
  return cuv

