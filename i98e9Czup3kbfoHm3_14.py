
def text_to_number_binary(txt):
  res = ""
  for w in txt.lower().split():
    if w == "one":
      res += '1'
    elif w == "zero":
      res += '0'
  if len(res) % 8 == 0:
    return res
  else:
    return res[:8*(len(res)//8)]

