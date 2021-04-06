
def staircase(n):
  stair = ""
  lst = []
  case = [n-1, -1, -1]
  if n < 0:
    n = -n
    case = [0, n, 1]
​
  for i in range(case[0], case[1], case[2]):
    stair += "_" * i + "#" * (n-i)
    lst.append(stair)
    stair = ""
​
  return "\n".join(lst)

