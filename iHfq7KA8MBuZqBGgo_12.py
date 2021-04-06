
def is_legitimate(backyard):
  if 1 in backyard[0] or 1 in backyard[-1]:
    return False
​
  left_fence = [backyard[i][0] for i in range(len(backyard))]
  right_fence = [backyard[i][-1] for i in range(len(backyard))]
  if 1 in left_fence or 1 in right_fence:
    return False
  return True

