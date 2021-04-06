
def is_there_consecutive(lst, n, times):
  return n not in lst if times==0 else any([lst[i:i+times]==[n]*times for i in range(len(lst))])

