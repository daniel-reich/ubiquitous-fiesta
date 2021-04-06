
def get_drink_ID(flavor, ml):
    a = ''.join((ch if ch in '0123456789 -e' else '') for ch in ml)
    words = ''.join([x[0:3] for x in flavor.split()])
    return str(words).upper() + a

