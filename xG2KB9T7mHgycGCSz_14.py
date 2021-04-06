
def valid(txt):
    return True if len(txt) in [4,6] and all(i.isnumeric() for i in txt) else False

