
def find_broken_keys(txt1, txt2):
  broken = []
  for x in range(len(txt1)):
    if txt1[x] != txt2[x] and txt1[x] not in broken:
      broken.append(txt1[x])
  return broken

