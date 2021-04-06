
def arrow(num):
  arrows = [">" * count for count in range(1, num + 1)]
  return arrows[:-1] + arrows[::-1] if num % 2 else arrows + arrows[::-1]

