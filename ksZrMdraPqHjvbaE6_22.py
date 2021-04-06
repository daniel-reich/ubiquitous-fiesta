
def largest_even(lst):
  even = [num for num in lst if num%2==0]
  even.sort()
  return -1 if len(even)==0 else even[-1]

