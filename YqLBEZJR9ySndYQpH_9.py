
def staircase(n):
  if n > 0:
    floor_list = ["_"*(n-floor) + "#"*floor + "\n" for floor in range(1, n+1)]
  else :
    floor_list = ["_"*floor + "#"*(abs(n)-floor) + "\n" for floor in range(abs(n))]
  return "".join([str(floor) for floor in floor_list])[:-1]

