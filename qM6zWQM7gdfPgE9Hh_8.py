
def filter_by_rating(d, rating):
  Filtered = {i:d[i] for i in d if d[i] == rating}
  if Filtered == {}:
    return "No results found"
  return Filtered

