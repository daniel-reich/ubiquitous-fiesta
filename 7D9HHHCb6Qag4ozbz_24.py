
def find_zip(txt):
  lst = txt.split('zip',2)  
  if len(lst) > 2:
    return len(lst[0]) + 3 + len(lst[1])
  else:
    return -1

