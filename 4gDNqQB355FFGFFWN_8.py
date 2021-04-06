
def available_spots(lst, num):
  return sum(lst[x]%2==num%2 or lst[x-1]%2==num%2 for x in range(1,len(lst)))

