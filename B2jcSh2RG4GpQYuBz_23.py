
def is_valid_phone_number(txt):
  return txt[0] == "(" \
           and txt[1:4].isnumeric() \
           and txt[4] == ")" \
           and txt[5] == " " \
           and txt[6:9].isnumeric() \
           and txt[9] == "-" \
           and txt[10:].isnumeric()

