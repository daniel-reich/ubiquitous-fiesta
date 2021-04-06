
def secret(text):
  return "<{}></{}>".format(text[:text.find("*")], text[:text.find("*")]) * int(text[text.find("*")+1:])

