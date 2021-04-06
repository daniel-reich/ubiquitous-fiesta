
def full_key_name(piece):
  x = 1 if piece[piece.rfind(" ")+1].isupper() else 0
  return (piece[:piece.rfind(" ") + 1] + piece[piece.rfind(" ") + 1].upper() + piece[piece.rfind(" ") + 2:] + "{}").format([" minor", " major"][x])

