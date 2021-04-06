
def alternating_caps(txt):
  is_cap = True
  new_txt = ""
  for letter in txt:
    if letter != " ":
      if is_cap:
        new_txt += letter.upper()
        is_cap = False
      else:
        new_txt += letter.lower()
        is_cap = True
    else:
      new_txt += " "
  return new_txt

