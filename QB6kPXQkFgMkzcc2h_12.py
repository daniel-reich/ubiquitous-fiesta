
def remove_abc(txt):
  orig = txt
  for i in 'abc':
    txt = txt.replace(i, '')
  return None if orig == txt else txt

