
def is_there_consecutive(lst, n, t):
  return n!=lst[0] if (len(lst)==1 and t==0) else any(lst[i:i+t]==[n]*t for i in range(len(lst)-t))

