
def decode(txt):
  output = []
  for ASCII_code in [str(ord(i)) for i in txt]:
    number = 0
    for digit in ASCII_code:
      if int(digit) > 0: number += int(digit)
    output.append(number)
  return output

