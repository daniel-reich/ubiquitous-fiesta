
def get_name(address):
  name = ""
  potition = address.find("@")
  for i in range(0, potition):
    if address[i] >= "A" and address[i] <= "Z" or address[i] >= "a" and address[i] <= "z":
      name += address[i]
  return name

