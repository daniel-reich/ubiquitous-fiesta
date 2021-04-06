
def get_items_at(r,s):
  try:return get_items_at(r[:-2],s)+[r[-(1+(s<'o'))]]
  except:return[]

