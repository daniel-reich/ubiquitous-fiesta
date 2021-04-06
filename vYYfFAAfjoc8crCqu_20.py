
def tree(h):
  return ["#".center(h * 2 - 1) if i == 0 else str("#" * ((i + i) + 1)).center(h * 2 - 1) for i in range(h)]

