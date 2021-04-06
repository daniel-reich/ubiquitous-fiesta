
def pop(state):
  lst = [i for i in range(max(state) + 1)]
  return lst[:-1] + lst[::-1]

