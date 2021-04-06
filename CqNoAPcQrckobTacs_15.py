
def missing_letter(lst):
  start = ord(lst[0])
  count = 0
  while start + count == ord(lst[count]):
    count += 1
  return chr(start + count)

