
def iso_group(lst):
  if len(lst)==1: return lst[0]
  meh = iso_group(lst[1:])
  if type(meh)==int: return meh if meh>lst[0] else lst[0] if meh<lst[0] else [meh,meh]
  else: return meh if meh[0]>lst[0] else lst[0] if meh[0]<lst[0] else [lst[0]]+meh

