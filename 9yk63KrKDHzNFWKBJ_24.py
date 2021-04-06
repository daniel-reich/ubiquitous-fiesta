
def is_it_inside(folders, X, Y):
  s=[]
  switch=True
  if X==Y:
    return True
  for key,value in folders.items():
    if key==Y:
      while(True):
        if len(s)>0:
          z=s
          s=[]
          switch=False
        else:
          if switch==False:
            return False
          else:
            z=folders[key]
        for f in range(len(z)):
          switch=False
          if X in z:
            return True
          if z[f] in folders.keys():
            for w in folders[z[f]]:
              s.append(w)
            if X in s:
              return True
          if f==len(z)-1:
            print(s)
            break
  return False

