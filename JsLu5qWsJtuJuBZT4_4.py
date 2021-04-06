
def flip(string, spec):
  if spec == "word":
    x = [word[::-1] for word in string.split()]
    x = " ".join(x)
    return x
  else:
    y = " ".join(string.split()[::-1])
    return y

