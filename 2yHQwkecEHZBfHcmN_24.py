
def progress_days(runs):
  count = 0
  for i in range(len(runs)):
    if i == len(runs) - 1:
      return count
    else:
      if runs[i + 1] > runs[i]:
        count += 1

