
def oddeven(lst):
  odd_count = sum(1 for element in lst if element%2==1)
  even_count = len(lst)-odd_count
  return odd_count>even_count

