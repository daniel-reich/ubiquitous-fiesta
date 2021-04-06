
def available_spots(lst, num):
  return sum([int(lst[i] % 2 == num % 2 or lst[i+1] % 2 == num % 2) for i in range(len(lst) - 1)])

