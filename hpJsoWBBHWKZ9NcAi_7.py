
def bird_code(lst):
  def encoding(name):
    name = [w.upper() for w in name.replace('-',' ').split()]
    if len(name)==1: return name[0][:4]
    if len(name)==2: return name[0][:2] + name[1][:2]
    if len(name)==3: return name[0][0] + name[1][0] + name[2][:2]
    else: return name[0][0] + name[1][0] + name[2][0] + name[3][0]
  return list(map(encoding, lst))

