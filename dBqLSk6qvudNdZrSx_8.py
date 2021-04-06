
def is_boiling(temp):
  return int(temp[:-1]) >= 212 if temp[-1] == 'F' else int(temp[:-1]) >= 100

