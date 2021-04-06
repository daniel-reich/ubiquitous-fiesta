
def full_key_name(piece):
  mm = [" major", " minor"]
  lst = piece.split()
  end = lst[-1]
  if end.istitle():
    return piece + mm[0]
  else:
    return " ".join(lst[:-1]) +" "+ end.title() + mm[1]

