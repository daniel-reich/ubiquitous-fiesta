
def divisible_by_left(n):
  div_left = [False]
  n = str(n)
  for i in range(1, len(n)):
    try:
      if int(n[i]) % int(n[i - 1]) == 0:
        div_left.append(True)
      else:
        div_left.append(False)
    except:
      div_left.append(False)
  return div_left

