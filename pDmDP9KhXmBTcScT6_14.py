
def get_name(address):
  name = address.split("@")[0]
  return "".join([i for i in name if i.isalpha()])

