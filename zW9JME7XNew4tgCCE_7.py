
def reversible_inclusive_list(start_of_range, end_of_range):
  if start_of_range < end_of_range:
    return list(range(start_of_range, end_of_range+1))
  return sorted(list(range(end_of_range, start_of_range+1)), reverse=True)

