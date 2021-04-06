
def is_there_consecutive(lst, n, times):
  while True:
    c = [n for _ in range(times)]
    flag = lst[:len(c)] == c
    if times == 0 and n in lst:
      return False 
    if flag:
      return True 
    try:
      for i in range(len(c)):
        lst.pop(0)
    except IndexError:
      return False

