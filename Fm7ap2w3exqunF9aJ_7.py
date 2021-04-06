
def count_lone_ones(n):
  n = '0' + str(n) + '0'
  return sum([n[i] == '1' and '1' not in [n[i-1], n[i+1]] for i in range(1, len(n) - 1)])

