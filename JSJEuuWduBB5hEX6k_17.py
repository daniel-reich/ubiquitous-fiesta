
def XO(text):
  lower_text = text.lower()
  num_x = 0
  num_o = 0
  for c in lower_text:
    if c == 'x':
      num_x += 1
    elif c == 'o':
      num_o += 1
  return num_x == num_o

