
def pirates_killed(gold, tolerance):
  for i in zip(gold, tolerance):
    if max(gold) - i[0] > i[1]:
      return True
  return False

