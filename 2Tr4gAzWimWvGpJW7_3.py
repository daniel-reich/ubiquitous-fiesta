
def is_there_consecutive(lst, n, times):
  return ''.join(str(n) for i in range(times)) in ''.join(map(str, lst))

