
def filter_by_rating(d, rating):  
  final_dict = dict()
  for key in d.keys():
    if len(d[key]) == len(rating):
      final_dict[key] = d[key]
  return "No results found" if len(final_dict) == 0 else final_dict

