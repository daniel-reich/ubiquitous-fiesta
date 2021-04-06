
def valid_name(name):
  lst = name.split()
  if len(lst) > 3 or len(lst) < 2:
    return False
  elif len([word for word in lst if word[0].isupper()]) != len(lst):
    return False
  elif len([word for word in lst if len(word) == 1 or (len(word) > 2 and '.' in word) or (len(word) == 2 and word[1] != '.')]) > 0:
    return False
  elif len(lst[len(lst) - 1]) < 2 or '.' in lst[len(lst) - 1]:
    return False
  elif '.' in lst[0] and '.' not in lst[1] and len(lst) == 3:
    return False
  return True

