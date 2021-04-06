
def double_swap(txt, c1, c2):
  result = ''
  for letter in txt:
    if letter == c1:
      result += c2
    elif letter == c2:
      result += c1
    else:
      result += letter
  return result

