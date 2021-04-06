
def remove_special_characters(txt):
  return "".join(i for i in txt if i.lower() in " abcdefghijklmnopqrstuvwxyz0123456789-_")

