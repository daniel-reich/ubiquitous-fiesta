
def spin_around(lst):
  return abs(sum(1 if turn == "right" else -1 for turn in lst)) // 4

