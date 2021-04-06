
def is_valid_PIN(pin):
    return len(pin) in (4, 6) and all(p in '0123456789' for p in pin)

