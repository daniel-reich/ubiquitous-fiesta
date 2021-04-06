
def redundant(s):
    msg = s
    def inner():
        return msg
    return inner

