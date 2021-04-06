
def find_a_seat(n, lst):
  max_seat = n // len(lst)
  
  try:
    return [lst.index(i) for i in lst if i <= max_seat/2][0]
  except:
    return -1

