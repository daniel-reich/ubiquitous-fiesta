
def is_wristband(lst):
  return all(i==i[::-1] for i in lst) or all(lst[i]==lst[-(i+1)] for i in range(len(lst))) or all(lst[i][1:]==lst[i-1][:-1] for i in range(1, len(lst))) or all(lst[i][:-1]==lst[i-1][1:] for i in range(1, len(lst)))

