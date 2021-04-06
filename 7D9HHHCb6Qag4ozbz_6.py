
def find_zip(txt):
  if txt.count('zip') < 2:
    return -1
  else:
    return [x for x in range(len(txt)) if txt[x] == 'z' and txt[x+1] == 'i' and txt[x+2] == 'p'][1]

