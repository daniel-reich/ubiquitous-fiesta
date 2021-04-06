
def is_checkerboard(lst):
  p = lst[0]
  for r in range(1, len(lst)):
      for i in range(len(lst[r])):
          if lst[r][i] == p[i]:
              return False
      p = lst[r]
  return True

