
def char_count(txt1, txt2):
  count = 0
  for c in txt2:
    if txt1 == c:
      count += 1
  return count

