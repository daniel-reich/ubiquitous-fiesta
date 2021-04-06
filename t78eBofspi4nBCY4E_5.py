
def base_conv(n,b):
  new_number = []
  if type(n) == int:
    number = ""
    power = 0
    while b ** (power+1) < n:
      power += 1
    for i in range(power, -1, -1):
      new_number.append(n // (b ** i))
      n -= (b ** i)*new_number[-1]
    for i in new_number:
      number += chr(i+97)
    return number
  else:
    number = 0
    new_number = [ord(i)-97 for i in n]
    for i in new_number:
      if i >= b or i < 0:
        return "{0} is not a base {1} number.".format(n,b)
    for i in range(len(new_number)):
      number += b**i*new_number[-1-i]
    return number

