
def is_there_consecutive(lst, n, times):
  lst = ''.join(str(i) for i in lst)
  
  return str(n) not in lst if times == 0 else str(n)*times in lst

