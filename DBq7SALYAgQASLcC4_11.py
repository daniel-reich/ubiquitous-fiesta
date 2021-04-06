
def char_count(txt1, txt2):
  count = 0
  for x in range(len(txt2) - len(txt1) + 1):
    if txt1 == txt2[x:x+len(txt1)]:
      count += 1
  return count

