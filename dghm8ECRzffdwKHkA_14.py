
def capital_letters(txt):
  count = 0
  for i in txt:
    if ord(i)>=65 and ord(i)<=90:
      count+=1
  return count

