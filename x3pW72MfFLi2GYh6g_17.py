
def is_scalable(lst):
  try:
    for idx, i in enumerate(lst):
      if i not in range(lst[idx + 1] - 6, lst[idx + 1] + 6):
        return False
  except IndexError:
    return True

