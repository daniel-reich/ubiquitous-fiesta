
def secret(txt):
  return "<{} class='{}'></{}>".format(txt.split('.')[0]," ".join(txt.split('.')[1:]),txt.split('.')[0])

