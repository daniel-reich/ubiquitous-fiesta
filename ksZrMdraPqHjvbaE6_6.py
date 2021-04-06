
def largest_even(lst):
  largest = -1
  for num in lst:
    if num % 2 == 0 and num > largest:
      largest = num
  return largest

