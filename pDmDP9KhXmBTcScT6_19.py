
def get_name(address):
  name = ''
  address = address.split("@")
  for i in address[0]:
    if i.isalpha():
      name += i
  return name

