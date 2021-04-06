
def count_number(r, c=0):
  if not r: return c
  if type(r[0]) is list:
    r[0] = [x for x in r[0]]
    return count_number(r[0]+r[1:], c)
  if type(r[0]) in [float, int]: c += 1
  return count_number(r[1:], c)

