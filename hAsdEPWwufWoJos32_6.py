
def no_yelling(phrase):
  count = 0
  n = -1
  while phrase[n] == "!" or phrase[n] == "?":
    count += 1
    n -= 1
  return phrase[:len(phrase) +1 - count]

