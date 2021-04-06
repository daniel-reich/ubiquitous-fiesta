
def filter_by_rating(d, rating):
  rate = {}
  if rating not in d.values():
    return 'No results found'
  else:
    for i in d:
      if d[i] == rating:
        rate.update({i:d[i]})
    return rate

