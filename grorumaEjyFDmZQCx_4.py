
def is_wristband(lst):
​
  func = lambda x: all(len(set(i)) == 1 for i in x)
  for fnc in [lst, zip(*lst)]:
    if func(fnc):
      return True
  
  for item, item_ in [(lst[1:], lst), (lst, lst[1:])]:
    if all(val_[1:] == val[:-1]
        for val, val_ in zip(item, item_)):
            return True
  return False

