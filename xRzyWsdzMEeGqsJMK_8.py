
def maskify(txt):
  return "".join([txt[c] if c>=len(txt)-4 else "#" for c in range(len(txt))])

