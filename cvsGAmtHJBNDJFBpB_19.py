
def can_traverse(x):
  new_traverse = list(zip(*x))
  for i in range(0,8):
      if sum(new_traverse[i+1]) - sum(new_traverse[i]) in range(-1,2):
        pass
      else:
        return False
  return True

