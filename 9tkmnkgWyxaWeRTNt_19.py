
def median(lst):
  return sorted(lst)[len(lst) // 2] if len(lst) % 2 != 0 else (sorted(lst)[len(lst)//2] + sorted(lst)[len(lst)//2 - 1]) / 2

