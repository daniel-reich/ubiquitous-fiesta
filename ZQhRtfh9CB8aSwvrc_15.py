
def greater_than_sum(num):
  return all(num[i]>sum(num[:i]) for i in range(1, len(num)))

