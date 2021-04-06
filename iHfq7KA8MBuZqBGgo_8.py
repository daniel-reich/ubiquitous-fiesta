
def is_legitimate(lst):
  if ((len(set(lst[0])) == 1 == len(set(lst[-1]))) and (list(set(lst[0]))[0] == 0 == list(set(lst[-1]))[0])):
    return all([i[0] == 0 ==i[-1] for i in lst])
  else:
    return False

