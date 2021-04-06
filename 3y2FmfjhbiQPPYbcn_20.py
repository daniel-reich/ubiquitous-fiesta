
def pop(state):
  half = [i for i in range(1 + len(state) // 2)]
  return half + half[:-1][::-1]

