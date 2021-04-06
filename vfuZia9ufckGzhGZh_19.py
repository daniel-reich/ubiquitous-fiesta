
def differences(lst):
  return [lst[i] - lst[i - 1] for i in range(1, len(lst))]
​
def seq_level(lst):
  res = ["Linear", "Quadratic", "Cubic"]
  diff = differences(lst)
  level = 0
  while len(set(diff)) > 1:
    diff = differences(diff)
    level += 1
  return res[level]

