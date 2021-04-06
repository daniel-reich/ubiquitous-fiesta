
def high_low(txt):
  num_list = [int(num) for num in txt.split()]
  return "{} {}".format(max(num_list), min(num_list))

