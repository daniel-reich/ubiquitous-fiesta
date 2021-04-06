
def bird_code(lst):
  bnames=[]
  for name in lst:
    ltmp = name.replace("-"," ").split()
    if len(ltmp) == 1 : bnames.append(ltmp[0][:4].upper())  
    if len(ltmp) == 2 : bnames.append(ltmp[0][:2].upper()+ltmp[1][:2].upper())
    if len(ltmp) == 3 : bnames.append(ltmp[0][:1].upper()+ltmp[1][:1].upper()+ltmp[2][:2].upper())
    if len(ltmp) == 4 : bnames.append(ltmp[0][:1].upper()+ltmp[1][:1].upper()+ltmp[2][:1].upper()+ltmp[3][:1].upper())
  return bnames

