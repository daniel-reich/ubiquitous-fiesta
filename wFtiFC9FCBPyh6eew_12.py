
def partitions(n):
  if n <= 1:
    return 1
  parts = [(n, [n])]
  trials = []
  for i in range(1,n//2+1):
    trials.append((i, [i]))
  while len(trials) > 0:
    trial = trials.pop()
    for i in range(trial[0],n-trial[0]+1):
      if sum(trial[1]) + i <= n:
        newTrial = (i,trial[1].copy())
        newTrial[1].append(i)
        if sum(newTrial[1]) == n:
          parts.append(newTrial)
        else:
          trials.append(newTrial)
  return len(parts)
  
  print("testing")
  print(partitions(0))

