
def find_broken_keys(txt1, txt2):
  lst = []
  
  for i in range(len(txt1)):
    if txt1[i] != txt2[i] and txt1[i] not in lst: lst.append(txt1[i])
  
  return lst

