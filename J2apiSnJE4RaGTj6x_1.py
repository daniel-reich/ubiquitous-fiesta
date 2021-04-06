
def find_broken_keys(txt1, txt2):
  broken=[]
  for i in range(len(txt1)):
    if txt2[i]!=txt1[i] and txt1[i] not in broken:
      broken.append(txt1[i])
  return broken

