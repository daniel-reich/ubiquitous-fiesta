
def is_boiling(temp):
  return temp[-1] == "C" and int(temp[:-1]) >= 100 \
  or temp[-1] == "F" and int(temp[:-1]) >= 212

