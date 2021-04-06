
def almost_sorted(lst):
  if lst==sorted(lst) or lst==sorted(lst)[::-1]:
    return False 
  else:
    a = [lst[:i]+lst[i+1:]==sorted(lst[:i]+lst[i+1:]) or 
    lst[:i]+lst[i+1:]==sorted(lst[:i]+lst[i+1:])[::-1] for i in range(len(lst))]
    return any(a)

