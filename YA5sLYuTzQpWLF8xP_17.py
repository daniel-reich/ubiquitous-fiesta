
def clean_up_list(lst):
  evens = [int(el) for el in lst if int(el) % 2 == 0]
  odds = [int(el) for el in lst if int(el) % 2 == 1]
  return [evens, odds]

