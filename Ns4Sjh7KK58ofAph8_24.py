
def is_triplet(n1, n2, n3):
  numbers = [n1,n2,n3]
  largest = max(numbers)
  count = 0
  for num in numbers:
    if num != largest:
      count += num**2
  return count == largest**2

