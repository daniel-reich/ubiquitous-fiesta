
def is_valid_PIN(pin):
  return (pin.isdecimal() and (len(pin) == 4 or len(pin) == 6))

