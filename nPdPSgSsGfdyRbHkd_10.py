
def hacker_speak(txt):
  text = ""
  for t in txt:
    if t == 'a':
      text += "4"
    elif t == 'e':
      text += "3"
    elif t == 'i':
      text += "1"
    elif t == 'o':
      text += "0"
    elif t == 's':
      text += "5"
    else:
      text += t
  return text

