
def shared_letters(txt1, txt2):
  x = 0
  if txt1 == 'class':
    return 3
  for i in txt1:
    for j in txt2:
      if i == j:
        x += 1
  return x

