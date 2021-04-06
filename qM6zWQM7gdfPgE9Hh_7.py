
def filter_by_rating(d, rating):
  
  new_d = dict()
  
  for key in d.keys():
    if d[key] == rating:
      new_d[key] = rating
      
  return "No results found" if not len(new_d) else new_d

