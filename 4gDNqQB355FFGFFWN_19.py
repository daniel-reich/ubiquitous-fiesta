
def available_spots(lst, num):
  count = 0
  for i in range(1, len(lst)):
    if lst[i-1] % 2 == num % 2 or lst[i] % 2 == num % 2:
      count += 1
  return count

