
def flipping_bits(n):
  binary = "{:0>32}".format(bin(n)[2:])
  result = ""
  for num in binary:
    if num == "0":
      result += "1"
    else:
      result += "0"
  return int(result, 2)

