
def keyboard_shortcut(txt):
  out = ''
  clipboard = ''
  i = 0
  while i < len(txt):
    if i < len(txt) + 8 and txt[i:i+9] == ' Ctrl + C':
      clipboard = ' ' + out
      i += 9
    elif i < len(txt) + 8 and txt[i:i+9] == ' Ctrl + V':
      out += clipboard
      i += 9
    else:
      out += txt[i]
      i += 1
  return out

