
def check_pattern(lst, pattern):
  d={}
  z=""
  m=[]
  for l in range(len(lst)):
    for e in lst[l]:
      z=z+str(e)
    if l==len(lst)-1:
      if z in d.keys():
        if d[z] != pattern[l]:
          return False
        else:
          break
      else:
        if pattern[l] in m and z not in d.keys():
          return False
        d[z]=pattern[l]
        m.append(pattern[l])
        break
    else:
      if z in d.keys():
        if d[z] != pattern[l]:
          return False
        else:
          z=""
          continue
      else:
        if pattern[l] in m and z not in d.keys():
          return False
        d[z]=pattern[l]
        z=""
        m.append(pattern[l])
  return True

