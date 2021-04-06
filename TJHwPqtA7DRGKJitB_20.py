
def is_prob_matrix(arr):
​
    condition_1 = True
    for raw in arr:
      if len(raw) != len(arr):
        condition_1 = False
        break
​
    condition_2 = True
    for raw in arr:
      for item in raw:
        if item < 0 or item > 1:
          condition_2 = False
          break
​
    condition_3 = True
    for raw in arr:
      if sum(raw) != 1:
        condition_3 = False
        break
​
    if condition_1 is True and condition_2 is True and condition_3 is True:
      return True
    else:
      return False

