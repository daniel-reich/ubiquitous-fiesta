
def reversible_inclusive_list(start_of_range, end_of_range):
  return [i for i in range(end_of_range, start_of_range + 1)][::-1] if end_of_range < start_of_range else \
    [i for i in range(start_of_range, end_of_range + 1)]

