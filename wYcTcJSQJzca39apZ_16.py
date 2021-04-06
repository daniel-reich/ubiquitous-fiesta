
def truncate(txt, length):
  lst=[]
  if length>len(txt):
    return txt
  for i in txt[:length].split(" "):
    lst.append(i)
  if txt[length].isalnum():
    new_lst = lst[:-1]
    return " ".join(new_lst)
  return " ".join(lst)

