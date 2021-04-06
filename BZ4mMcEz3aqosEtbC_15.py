
def mean(num):
  num_arr = list(map(lambda d: int(d), str(num)))
  return sum(num_arr) / len(num_arr)

