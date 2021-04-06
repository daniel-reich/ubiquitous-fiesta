
def filter_by_rating(d, rating):
  k = {key:value for key, value in d.items() if value == rating}
  return 'No results found' if len(k)==0 else k

