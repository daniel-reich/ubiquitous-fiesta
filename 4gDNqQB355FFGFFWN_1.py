
def available_spots(lst, num):
  m = num%2
  return sum(1 if (lst[i]%2==m or lst[i-1]%2==m) else 0 for i in range(1, len(lst)))

