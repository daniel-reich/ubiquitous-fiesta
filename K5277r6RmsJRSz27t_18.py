
def emphasise(txt):
  return "".join([txt[i].upper() if i == 0 or txt[i - 1] == " " and isinstance(txt[i], str) else txt[i].lower() if isinstance(txt[i], str) else txt[i] for i in range(0, len(txt))])

