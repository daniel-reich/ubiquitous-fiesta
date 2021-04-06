
def strictly_increasing(arr):
  return all(x < y for x,y in zip(arr, arr[1:]))
  
def can_see_stage(seats):
  transpose = list(zip(*seats))
  return all(strictly_increasing(x) for x in transpose)

