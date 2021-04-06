
def possible_path(lst):
  room = {
  1: [2],
  2: [1,"H"],
  3: [4],
  4: [3,"H"],
  "H": [2,4]
  }
  for i in range(len(lst)-1):
    if lst[i+1] not in room[lst[i]]:
      return False
  return True

