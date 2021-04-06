
def emotify(txt):
  dic = {
    "smile":":D",
    "grin":":)",
    "sad":":(",
    "mad":":P"
  }
  return "Make me " + dic[txt.split(" ")[-1]]

