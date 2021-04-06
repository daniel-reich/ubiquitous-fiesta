
def filter_by_rating(d, rating):
  return {i: k for i, k in d.items() if k == rating} if rating in d.values() else "No results found"

