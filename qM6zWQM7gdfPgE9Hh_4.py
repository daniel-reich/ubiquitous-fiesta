
def filter_by_rating(d, rating):
  new_dict = {}
  for name, star_rating in d.items():
    if star_rating == rating:
      new_dict[name] = star_rating
  if len(new_dict) > 0:
    return new_dict
  else:
    return "No results found"

