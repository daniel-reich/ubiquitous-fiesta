
def longest_run(lst):
  def check(lst):
    runs = []
    i = 0
    run = []
    while i < len(lst):
      if i == len(lst) - 1:
        run.append(lst[i])
        runs.append(run)
        break
      if lst[i]+1 == lst[i+1]:
        run.append(lst[i])
        i += 1
      else:
        run.append(lst[i])
        runs.append(run)
        run = []
        i += 1
    lens = [len(run) for run in runs]
    return max(lens)
  one = check(lst)
  lst.reverse()
  two = check(lst)
  if two >= one:
    return two
  return one

