
def is_there_consecutive(lst, n, times):
  if times == 0:
    return n not in lst
  return [n] * times in [lst[i:i+times] for i in range(len(lst))]

