
def palindrome_type(deci):
  binary=bin(deci).replace("0b", "")
  if int(''.join(reversed(str(deci))))==deci:
    if ''.join(reversed(binary))==binary:
      return "Decimal and binary."
    else:
      return "Decimal only."
  elif ''.join(reversed(binary))==binary:
    return "Binary only."
  else:
    return "Neither!"

