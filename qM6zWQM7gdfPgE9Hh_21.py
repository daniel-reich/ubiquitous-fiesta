
def filter_by_rating(d, rating):
  res = {k : v for k, v in d.items() if v == rating}
  return res if len(res) else "No results found"

