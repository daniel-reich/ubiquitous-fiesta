
def happiness_number(s):
  happy = 0
  sad = 0
  happy += s.count(":)")
  happy += s.count("(:")
  sad -= s.count(":(")
  sad -= s.count("):")
  return happy + sad

