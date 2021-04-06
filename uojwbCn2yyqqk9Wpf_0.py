
def is_untouchable(number):
  if number < 2:
    return "Invalid Input"
  limit = ((number * number) + 1)
  k = [1] * limit
  for d in range(2, limit):
    for j in range(d + d, limit, d):
      k[j] += d
  if number not in k:
    return True
  return [i for i in range(len(k)) if k[i] == number]

