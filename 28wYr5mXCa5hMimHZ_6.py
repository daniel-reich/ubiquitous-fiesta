
def valid_name(name):
  n_lst = name.split(" ")
  if len(n_lst) < 2:
    return False
​
  in_or_name = []
  for string in n_lst:
    if "." in string:
      if len(string) > 2 or "." != string[1] or string[0].islower():
        return False
      else:
        in_or_name.append(0)
    else:
      if string != string.capitalize():
        return False
      else:
        in_or_name.append(1)
  if in_or_name in [[0,1],[0,0,1],[1,0,1],[1,1,1]]:
    return True
  else:
    return False

