
def filter_factorials(numbers):
  biggest, fact, i = max(numbers), 1, 1
  factorials = []
  while fact <= biggest:
    factorials.append(fact)
    fact *= i
    i += 1
  return [num for num in numbers if num in factorials]

