
def can_patch(bridge, planks):
  s=0
  c=0
  switch=False
  if len(planks)==0:
    switch=True
  for b in bridge:
    if b != 0:
      if c>s:
        s=c
      if c>0:
        if c-1 in planks:
          planks.remove(c-1)
        elif c in planks:
          planks.remove(c)
        else:
          if switch==True:
            c=0
            continue
          else:
            return False
        c=0
      else:
        c=0
    if b ==0:
      c+=1
  if s<=1 or switch==False:
    return True
  else:
    return False

