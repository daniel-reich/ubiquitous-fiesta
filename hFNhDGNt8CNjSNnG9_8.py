
def setify(lst):
  lst.sort()
  lst=list(dict.fromkeys(lst))
  lst.sort()
  return lst

