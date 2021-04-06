
def shared_letters(txt1, txt2):
  count = 0
  x = list(set(txt1))
  for i in range(len(x)):
    if x[i] in txt2:
      count += 1
  return count

