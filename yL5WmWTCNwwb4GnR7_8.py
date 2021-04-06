
def return_unique(lst):
  res = []
  counted = []
  for i in lst:
      if i not in counted:
          counted.append(i)
          if lst.count(i) == 1:
              res.append(i)
  return res

