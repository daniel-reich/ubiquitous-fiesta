
def digit_sort(lst):
  def lennum(x):
    return (-len(str(x)),x)
  return sorted(lst,key=lennum)

