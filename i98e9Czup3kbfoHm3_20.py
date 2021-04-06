
def text_to_number_binary(txt):
  out = ""
  for w in txt.split():
    if w.lower() == "zero":
      out += "0"
    elif w.lower() == "one":
      out += "1"
  
  if len(out) % 8 != 0:
    return out[0:int(len(out)/8)*8]
  else : return out

