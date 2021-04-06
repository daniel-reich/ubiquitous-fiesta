
def filter_by_rating(d, rating):
  if {k:v for k, v in d.items() if v == rating} == {}:
    return "No results found"
  return {k:v for k, v in d.items() if v == rating}

