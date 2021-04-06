
def longest_run(lst):
  concursive = []
  run = [lst[0]]
  for i in range(1, len(lst)):
    if lst[i-1] == lst[i] - 1:
      run.append(lst[i])
    else:
      concursive.append(run)
      run = [lst[i]]
  concursive.append(run)
  longest = max([len(c) for c in concursive])
  if longest == 1:
    concursive = []
    run = [lst[0]]
    for i in range(1, len(lst)):
      if lst[i-1] == lst[i] + 1:
        run.append(lst[i])
      else:
        concursive.append(run)
        run = [lst[i]]
    concursive.append(run)
    longest = max([len(c) for c in concursive])
  return longest

