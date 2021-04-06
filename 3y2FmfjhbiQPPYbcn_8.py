
def pop(state): #w/o built-in
  distance, length = state, 0
  while distance != []:
    length += 1
    distance = distance[1:]
  l, n, lst = length // 2, 0, []
  while n < state[l]:
    lst += [n]
    n += 1
  return lst + [l] + lst[::-1]
​
def pop(state): #w/ built-in
  splash = [x for x in range(0, max(state) + 1)]
  return splash + splash[:-1][::-1]

