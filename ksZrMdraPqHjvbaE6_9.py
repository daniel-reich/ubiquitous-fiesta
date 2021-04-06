
def largest_even(lst):
  even_numbers = [x for x in lst if x%2==0]
  return -1 if len(even_numbers) == 0 else max(even_numbers)

