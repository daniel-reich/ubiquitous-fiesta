
def filter_by_rating(d, rating):
  return {k:v for k,v in d.items() if v==rating} if rating in d.values() else "No results found"

