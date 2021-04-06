
def possible_path(lst):
  doors = ["12", "34", "2H", "4H"]
  pairs = []
  for i, room in enumerate(lst):
    if i == 0:
      continue
    pairs.append("".join(sorted(str(room)+str(lst[i-1]))))
  for pair in pairs:
    if not pair in doors:
      return False
  return True

