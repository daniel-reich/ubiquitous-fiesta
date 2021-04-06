
def keyboard_mistakes(txt):
  table=txt.maketrans('4501','ASOI')
  return txt.translate(table)

