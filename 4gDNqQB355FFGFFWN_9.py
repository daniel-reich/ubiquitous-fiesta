
def available_spots(lst, num):
  return sum([ (lst[idx-1] % 2) ==  num % 2 or (lst[idx] % 2 == num %2) for idx in range(1,len(lst)) ])

