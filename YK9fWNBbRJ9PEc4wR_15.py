
def tuck_in(lst1, lst2):
  a = round(len(lst1)/2)
  nlst1 = lst1[:a]
  nlst2 = lst1[a:]
  nlst1.extend(lst2)
  nlst1.extend(nlst2)
  return nlst1

