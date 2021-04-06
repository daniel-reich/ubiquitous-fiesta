
def power_of_two(num):
  return (num != 0) & ((num & (num - 1)) == 0)

