
def straight_digital(number):
  lst = list(map(int, list(str(abs(number)))))
  if len(set(lst)) == 1 and number > 100:
    return "Trivial Straight"
  diff = [j - i for i, j in zip(lst[:-1], lst[1:])]
  if len(set(diff)) == 1 and number > 100:
    return diff[0]
  return "Not Straight"

