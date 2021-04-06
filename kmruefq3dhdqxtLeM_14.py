
def sum_digits(a, b):
  digisum = 0
  for i in range(a, b + 1):
    for c in str(i):
      digisum += int(c)
  return digisum

