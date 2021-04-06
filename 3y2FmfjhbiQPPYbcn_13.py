
def pop(state):
  lst=[i for i in range(max(state)+1)]
  return lst+lst[-2::-1]

