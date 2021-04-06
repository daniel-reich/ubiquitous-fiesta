
def special_reverse_string(txt):
  upper_position = [c for c, i in enumerate(txt) if str(i).isalpha() and str(i).strip() and i.upper() == i]
  space_position = [c for c, i in enumerate(txt) if i == " "]
  txt = list(txt[::-1].lower().replace(" ", ""))
  for s in space_position:
      txt.insert(s, " ")
  for u in upper_position:
      txt[u] = txt[u].upper()
  return "".join(txt)

