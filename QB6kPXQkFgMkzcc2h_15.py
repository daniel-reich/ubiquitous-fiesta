
def remove_abc(txt):
  if 'a' in txt or 'b' in txt or 'c' in txt:
    txt = txt.replace('a', '')
    txt = txt.replace('b', '')
    txt = txt.replace('c', '')
    return txt
  else:
    return None

