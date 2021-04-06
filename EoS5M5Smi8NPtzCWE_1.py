
def secret(text):
    return "<{0}></{0}>".format(text.split("*")[0]) * int(text[-1])

