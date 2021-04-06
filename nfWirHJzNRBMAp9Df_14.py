
def hamming_distance(txt1, txt2):
  lst = tuple(zip(txt1, txt2))
  count = 0
  for list in lst:
    if list[0] != list[1]:
      count += 1
  return count

