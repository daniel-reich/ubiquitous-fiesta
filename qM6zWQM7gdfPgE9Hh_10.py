
def filter_by_rating(d, rating):
  dict = b = { key: value for key, value in d.items() if value == rating }
    
  if dict == {}:
    return 'No results found'
    
  else:
    return dict

