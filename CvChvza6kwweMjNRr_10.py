
def split_code(item):
  nums = list("123456789")
  letters = []
  digits = []
  for i in range(len(item)):
    if item[i] in nums:
      digits.append(item[i])
    else:
      letters.append(item[i])
  val = "".join(digits)
  val = int(val)
  return ["".join(letters), val]

