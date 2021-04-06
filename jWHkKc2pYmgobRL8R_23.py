
def distance_to_nearest_vowel(txt):
  r=["a","e","i","o","u"]
  fi=[]
  c=0
  switch=False
  for t in range(len(txt)):
    if txt[t] in r:
      fi.append(0)
      c=0
      switch=True
    else:
      if switch==True:
        c+=1
      v=1
      if t==len(txt)-1:
        fi.append(c)
        break
      for y in txt[t+1:]:
        if y not in r:
          v+=1
        if y in r:
          break
      if c<v and switch==True:
        fi.append(c)
      else:
        fi.append(v)
      v=0
  return fi

