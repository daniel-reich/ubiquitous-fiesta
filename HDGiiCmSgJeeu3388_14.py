
def choose_fuse(fuses, current):
  blank = []
  split = current.split('V')
  integer = float(split[0])
  for i in fuses:
    x = i.split('V')
    y = int(x[0])
    blank.append(y)
  blank.append(integer)
  new = sorted(blank)
  index = new.index(integer)
  return str(int(new[index+1]))+'V'

