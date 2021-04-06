
def grab_city(text):
  start = text.rfind('[')
  end = text.rfind(']')
  return text[start+1:end]

