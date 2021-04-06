
def shift_to_right(x, y):
  # recursive code here
  return x // 1 if not y else shift_to_right(x / 2, y - 1)

