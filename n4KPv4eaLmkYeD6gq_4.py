
def face_interval(num):
  lst = num
  if type(lst) == list:
    interv = max(lst) - min(lst)
    return ":)" if interv in lst else ":("
  else:
    return ":/"

