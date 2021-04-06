
def is_valid_PIN(pin):
  return (len(pin) == 4 or len(pin) == 6) and pin.isdigit()

