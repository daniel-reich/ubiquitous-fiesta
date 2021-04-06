
def make_happy(s):
  frown = [':(','8(','x(',';(']; smile = [':)','8)','x)',';)']
  for i in range(4):
    s = s.replace(frown[i],smile[i])
  return s

