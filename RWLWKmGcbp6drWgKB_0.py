
def chosen_wine(wines):
  if not wines: return None
  
  wines.sort(key=lambda x: x['price'])
  
  try:
    chosen = wines[1]['name']
  except IndexError:
    chosen = wines[0]['name']
    
  return chosen

