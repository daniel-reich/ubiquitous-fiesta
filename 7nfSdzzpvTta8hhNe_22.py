
def organize(txt):
  txt = txt.split(",")
  return {"age":int(txt[1]),"occupation":txt[2].strip(" "),"name":txt[0]} if len(txt) > 1 else {}

