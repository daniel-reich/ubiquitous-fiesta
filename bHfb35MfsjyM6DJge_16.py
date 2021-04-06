
def route_diff(directions):
  lst = [directions.count(foo) for foo in ["N", "S" , "E" , "W"]]
  return len(directions) - abs(lst[0] - lst[1]) - abs(lst[2] - lst[-1])

