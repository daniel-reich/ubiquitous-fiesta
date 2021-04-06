
from re import sub
length = len("Ctrl + C ")
def keyboard_shortcut(txt,copied = None):
  while True:
    if not "Ctrl +" in txt:
      return sub(r'\s{2,}|\s+$','',txt)
    index = txt.index("Ctrl +")
    if txt[index+7] == "C":
      copied = txt[:index]
      txt = txt[:index] + txt[index+length::]
    else:
      if copied:
        txt = txt[:index] + copied + txt[index+length::]
      else:
        txt = txt[:index] + txt[index+length::]

