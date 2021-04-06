
def filter_by_rating(d, rating):
  res = {}
  for k, v in d.items():
    if v == rating:
      res[k] = v
  return res if res else 'No results found'

