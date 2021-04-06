
def doubleton(n):
  while True:
    n += 1
    num_set = set()
    for num in str(n):
        num_set.add(num)
    if len(num_set) == 2:
        return n

