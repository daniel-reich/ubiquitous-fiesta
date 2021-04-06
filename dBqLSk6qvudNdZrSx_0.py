
def is_boiling(temp):
  t = int(temp[:-1])
  return t>=212 if 'F' in temp else t>=100

