
def bonacci(N, k):
  bonacci = [0 for i in range(N)] + [1]
  for i in range(k):
    bonacci += [sum(bonacci[-N:])]
  return bonacci[k]

