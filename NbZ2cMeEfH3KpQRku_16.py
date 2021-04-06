
def portion_happy(numbers):
  h = [0, 0]
  for i in range(1, len(numbers) - 1):
    if (numbers[i - 1] == numbers[i]) or (numbers[i + 1] == numbers[i]):
      h[numbers[i]] += 1
  if numbers[0] == numbers[1]:
    h[numbers[0]] += 1
  if numbers[-1] == numbers[-2]:
    h[numbers[-1]] += 1
  return (h[0] + h[1]) / len(numbers)

