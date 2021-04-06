
def dial(txt):
  txt = txt.lower()
  table = txt.maketrans("abcdefghijklmnopqrstuvwxyz",
            "22233344455566677778889999")
  return txt.translate(table)

