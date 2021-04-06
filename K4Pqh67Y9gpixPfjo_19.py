
def is_valid_PIN(pin):
    if (pin.isdigit() and (len(list(pin)) ==4 or len(list(pin)) ==6)):
        return(True)
    else:
        return(False)

