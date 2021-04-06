
def simple_numbers(a, b):
  simple_nums = []
  for i in range(a, b + 1):
    total = 0
    count = 1
    for j in str(i):
      total += int(j) ** count
      count += 1
    if total == i:
      simple_nums.append(i)
  return simple_nums

