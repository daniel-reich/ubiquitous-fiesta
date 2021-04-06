
def secret(text):
  x = text.split("*")
  return "<{}></{}>".format(x[0], x[0]) * int(x[-1])

