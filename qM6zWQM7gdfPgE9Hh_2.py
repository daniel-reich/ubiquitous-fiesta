
def filter_by_rating(d, rating):
  if rating not in d.values(): return 'No results found'
  return {k:v for k,v in d.items() if v==rating}

