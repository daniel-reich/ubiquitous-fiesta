
def convert_to_hex(txt):
  result = ""
  letters = list(txt)
  for l in letters:
    num = hex(ord(l))
    result += num[2:] + " "
  return result.strip()

