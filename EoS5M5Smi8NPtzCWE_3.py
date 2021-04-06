
def secret(text):
  a, b = text.split("*")
  return "<{}></{}>".format(a, a)*int(b)

