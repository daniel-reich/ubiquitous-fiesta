
def double_swap(txt, c1, c2):
  output = ""
  for char in txt:
    if char not in [c1, c2]:
      output += char
    else:
      if char == c1:
        output += c2
      else:
        output += c1
  return output

