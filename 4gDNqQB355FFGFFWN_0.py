
def available_spots(lst, num):
  return sum(1 for i, j in zip(lst, lst[1:]) if not (i%2==j%2!=num%2))

