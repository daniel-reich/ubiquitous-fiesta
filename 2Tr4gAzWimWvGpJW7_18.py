
def is_there_consecutive(lst, n, times):
  if times:
    return any(times*[n]==lst[i:i+times] for i in range(len(lst)))
  else:
    return n not in lst

