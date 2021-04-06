
def text_to_number_binary(txt):
  result = "".join(["1" if foo == "one" else "0" if foo == "zero" else "" for foo in txt.lower().split()])
  return result[:(len(result) - len(result) % 8)]

