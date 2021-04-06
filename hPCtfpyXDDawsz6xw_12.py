
def verbify(txt):
  txt1, txt2 = txt.split()[0], txt.split()[1]
  if txt1.endswith('ed'):
    return txt
​
  elif txt1.endswith('e'):
    return '{}d {}'.format(txt1, txt2)
​
  return '{}ed {}'.format(txt1,txt2)

