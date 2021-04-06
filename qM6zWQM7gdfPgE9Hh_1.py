
def filter_by_rating(d, rating):
  matched = {k:v for k, v in d.items() if v == rating}
  return matched or 'No results found'

