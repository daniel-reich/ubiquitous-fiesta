
def jazzify(lst):
  if not lst: return []
  for idx,el in enumerate(lst):
    if not el.endswith('7'):
      el+='7'
      lst[idx]=el
  return lst

