
def normalize(txt):
    return '{}!'.format(txt.lower().capitalize()) if txt.isupper() else txt

