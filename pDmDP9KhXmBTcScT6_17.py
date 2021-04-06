
def get_name(address):
  import string
  firstpart = address.split('@')[0]
  all_letters = string.ascii_letters
  x = ''.join([ch for ch in firstpart if ch in all_letters])
  return x

