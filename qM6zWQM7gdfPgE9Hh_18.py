
def filter_by_rating(d, rating):
  result = {item:rate for item,rate in d.items() if rate == rating}
  if result:
    return result
  return "No results found"

