
def parse_code(txt):
  txt = [i for i in txt.split("0") if bool(i)==True]
  return {"first_name": txt[0] ,"last_name": txt[1] ,"id": txt[2]}

