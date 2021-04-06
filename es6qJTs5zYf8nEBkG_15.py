
def is_rectangle(c):
  if len(set(c)) == 4:
    for i in range(len(c)):
      c[i] = [int(c[i][c[i].find("(")+1: c[i].find(",")]), int(c[i][c[i].find(",")+1: c[i].find(")")])]
    if len(set([x[0] for x in c])) == 2 and len(set([x[1] for x in c])) == 2:
      return True
  return False

