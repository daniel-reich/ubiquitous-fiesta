
def to_camel_case(text):
  text = text.replace('_','-')
  lst = text.split("-")
  return lst[0] + ''.join([i.capitalize() for i in lst[1:]])

