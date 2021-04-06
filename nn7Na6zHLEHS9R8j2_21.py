
def deep_count(lst):
    if not isinstance(lst,list):
        return 1
    s = 0
    for item in lst:
      if not isinstance(item,list):
        s = s + 1
      else:
        s = s + 1
        s = s + deep_count(item)
    return s

