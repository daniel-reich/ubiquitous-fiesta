
def final_countdown(lst):
  countdowns = []
  count = 0
  out = []
  for i in range(len(lst)):
    if lst[i] == 1:
      count += 1
      j = 1
      countdown = [1]
      while lst[i - j] == 1 + j:
        countdown.insert(0, j + 1)
        j += 1
      countdowns.append(countdown)
  out.append(count)
  out.append(countdowns)
  return out

