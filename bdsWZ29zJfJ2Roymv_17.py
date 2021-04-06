
def swap_two(txt):
  result, x= "", 0
  while x < len(txt):
    a, b = "", ""
    if x + 4 <= len(txt):
      a += txt[x]
      a += txt[x+1]
      b += txt[x+2]
      b += txt[x+3]
      a, b = b, a
      result += a + b
      x += 4
    else:
      result += txt[x]
      x += 1
  return result

