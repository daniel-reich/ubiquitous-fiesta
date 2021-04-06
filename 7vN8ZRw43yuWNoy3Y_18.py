
def parse_code(txt):
  while "00"in txt:
    txt = txt.replace("00", "0")
  txt = txt.split("0")
  return {"first_name": txt[0], "last_name": txt[1], "id": txt[2]}

