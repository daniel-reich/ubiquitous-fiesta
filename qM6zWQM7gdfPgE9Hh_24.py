
def filter_by_rating(d, rating):
  return {k: v for k,v in d.items() if len(v) == len(rating)} or 'No results found'

