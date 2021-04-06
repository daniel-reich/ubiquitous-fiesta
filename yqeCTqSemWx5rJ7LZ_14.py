
def full_key_name(piece):
  lst = piece.split("in ")
  return lst[0] + "in {}{} {}".format(lst[-1][0].upper(), "" if len(lst[-1]) == 1 else lst[-1][-1], "major" if lst[-1][0].isupper() else "minor")

