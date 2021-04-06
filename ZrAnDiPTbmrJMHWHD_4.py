
def is_central(txt):
  mid = len(txt)//2
  return txt[mid] != ' ' if len(txt) % 2 ==  1 else False

