
def balanced(lst):
  l = len(lst)//2
  f_h, s_h = lst[:l], lst[l:]
  return f_h * 2 if sum(f_h) > sum(s_h) else s_h * 2 if sum(s_h) > sum(f_h) else lst

