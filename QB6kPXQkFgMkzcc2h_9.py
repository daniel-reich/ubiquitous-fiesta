
def remove_abc(txt):
  if txt.find('a') == -1 and txt.find('b') == -1 and txt.find('c') == -1:
    return None
  return ''.join([i for i in txt if i not in 'abc'])

